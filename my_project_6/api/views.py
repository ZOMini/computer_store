from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from store.models import Category, Item, Name

from api.permissions import AdminOrReadOnly
from api.serializers import (CategorySerializer, CategorySerializerGet,
                             ItemSerializer, NameSerializer, NameSerializerGet)


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
            # print(f'--if name {self.action}')
            return NameSerializerGet
        # print(f'else action {self.action}')
        # print(f'else metod{self.request.method}')
        # category= self.kwargs.get('mod_name')
        # print(f'category_fail?{category}')
        return NameSerializer 
    
    def perform_create(self, serializer):
        category= self.request.data.get('category')
        # print(f'category_fail?{category}')
        category = get_object_or_404(Category, id=category)
        serializer.save(category = category)
