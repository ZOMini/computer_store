from django import forms

from .models import Category, Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'category', 'count_in_magaz', 'count_in_store', 'price', )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description',)
