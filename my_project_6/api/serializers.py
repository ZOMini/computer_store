from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from store.models import Category, Item, Name


class ItemSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    name = SlugRelatedField(slug_field='mod_name', read_only=True)
    
    class Meta:
        fields = '__all__'
        model = Item

class NameSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='title', read_only=True)
    model_items = ItemSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Name

class CategorySerializer(serializers.ModelSerializer):
    category_name = NameSerializer(read_only=True, many=True)
    
    class Meta:
        fields = '__all__'
        model = Category
