from django import forms

from magazine.models import Category, Item, Name


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'serial_num', 'status',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description',)

class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ('mod_name', 'price', 'mod_detail', 'category', 'image')
