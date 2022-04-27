from time import time

from django.shortcuts import render
from rest_framework import filters, permissions, viewsets
from store.models import Category, Item, Name

from api.permissions import AdminOrReadOnly
from api.serializers import CategorySerializer, ItemSerializer, NameSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly, )


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (AdminOrReadOnly, )

class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer
    permission_classes = (AdminOrReadOnly, )
