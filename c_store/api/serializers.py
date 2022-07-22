from requests import request
from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    Serializer,
    ValidationError
)

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

class PostItemsSerialSerializer(ModelSerializer):
    
    class Meta:
        fields = ('serial_num',)
        model = Item

    def create(self, validated_data):
        request = self.context.get('request')
        serial_num = validated_data.get('serial_num')
        author = request.user
        name_id = self.context.get('name_id')
        name = Name.objects.get(id=name_id)
        item = Item.objects.create(
            author=author,
            name=name,
            serial_num=serial_num,
        )
        item.save()
        return item

class AltDeleteItemsSerialSerializer(Serializer):
    serial_num = CharField(max_length=12, min_length=12)
    
    def validate(self, data):
        data_obj = data['serial_num']
        item = Item.objects.filter(serial_num = data_obj)
        if item.exists():
            return item
        else:
            raise ValidationError(f'{data_obj} - такой серийный номер отсутствует.')
