from rest_framework.relations import (PrimaryKeyRelatedField, SlugRelatedField,
                                      StringRelatedField)
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator
from store.models import Category, Item, Name


class ItemSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    name = SlugRelatedField(slug_field='mod_name', read_only=True)
    
    class Meta:
        fields = '__all__'
        model = Item

class NameSerializer(ModelSerializer):
    category = StringRelatedField(read_only=True)
    
    class Meta:
        fields = '__all__'
        model = Name

class NameSerializerGet(ModelSerializer):
    category = StringRelatedField(read_only=True)
    model_items = ItemSerializer(read_only=True, many=True)

    class Meta:
        fields = 'id', 'category', 'mod_name', 'price', 'mod_detail', 'mod_date', 'image', 'model_items'
        model = Name

class CategorySerializer(ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Category

class CategorySerializerGet(ModelSerializer):
    category_name = NameSerializerGet(read_only=True, many=True)
    
    class Meta:
        fields = 'id', 'title', 'description', 'category_name'
        model = Category
