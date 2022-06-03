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
        # print(f'else {self.action}')
        # print(f'else metod{self.request.method}')
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
        # category= self.kwargs.get('mod_name')
        # print(f'category_fail?{category}')
        return NameSerializer 
    
    def perform_create(self, serializer):
        category= self.request.data.get('category')
        # print(f'category_fail?{category}')
        category = get_object_or_404(Category, id=category)
        serializer.save(category = category)

class PostItemsSerialViews(views.APIView):
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

