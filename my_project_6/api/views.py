from distutils.log import error

from django.shortcuts import get_object_or_404
from rest_framework import (
    filters,
    mixins,
    permissions,
    status,
    views,
    viewsets
)
from rest_framework.response import Response

from api.permissions import AdminOrReadOnly
from api.serializers import (
    AltDeleteItemsSerialSerializer,
    CategorySerializer,
    CategorySerializerGet,
    ItemSerializer,
    NameSerializer,
    NameSerializerGet,
    PostItemsSerialSerializer
)
from store.models import Category, Item, Name


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly, )
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategorySerializerGet
        return CategorySerializer 

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (AdminOrReadOnly, )

class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer
    permission_classes = (AdminOrReadOnly, )
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NameSerializerGet
        return NameSerializer 
    
    def perform_create(self, serializer):
        category= self.request.data.get('category')
        category = get_object_or_404(Category, id=category)
        serializer.save(category = category)

class PostItemsSerialViews(views.APIView):
    """
    Гипотетическая необходимость создать Items одинаковой модели(Name),
    передавая в JSON только серийные номера, Name в слаге.
    """
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, name_id):
        data = request.data.get('model_items')
        serializer = PostItemsSerialSerializer(
            data=data, many=True,
            context={'name_id': name_id, 'request': request})
        if serializer.is_valid():
            serializer.save()
            serializer = ItemSerializer(
                instance=serializer.instance,
                context={'request': self.request},
                many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteItemsSerialViews(views.APIView):
    """
    Гипотетическая необходимость удалить любые Items,
    передавая в JSON только серийные номера.
    Upd. Удаляет все Items которые найдет,
    остальные вернет с ошибкой.
    """
    permission_classes = (permissions.IsAdminUser,)

    def delete(self, request):
        data_set = request.data.get('model_items')
        data_success = {}
        lists_error = []
        for data in data_set:
            item_serial = data['serial_num']
            if Item.objects.filter(serial_num = item_serial).exists():
                data_success[item_serial] = 'Item успешно удален'
                Item.objects.filter(serial_num = item_serial).delete()
            else:
                lists_error.append({'serial_num': item_serial})
                data_success['error'] = lists_error
        if 'error' in data_success:
            data_success['error_info'] = 'серийные(й) номера отсутствуют.'
            i_status = status.HTTP_400_BAD_REQUEST
        else:
            i_status = status.HTTP_204_NO_CONTENT
        return Response(data_success, status=i_status)  

class AltDeleteItemsSerialViews(views.APIView):
    """
    Альтернативный метод удаления по серийникам.
    Удаляет только если все серийные номера - валидны.
    """
    permission_classes = (permissions.IsAdminUser,)

    def delete(self, request):
        data_set = request.data.get('model_items')
        serializer = AltDeleteItemsSerialSerializer(
            data=data_set, many=True)
        serializer.is_valid(raise_exception=True)
        for data in serializer.validated_data:
            data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
