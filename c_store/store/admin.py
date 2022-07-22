from django.contrib import admin

from store.models import Category, Item, Name


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'serial_num',
        'status',
        'phone',
        'pub_date',
        'author',
    )
    # list_editable = ('category','price')
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '--Пусто--'
    list_select_related = ('author',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    empty_value_display = '--Пусто--'

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mod_name', 'mod_detail', 'category', 'image')
    search_fields = ('mod_name',)
    empty_value_display = '--Пусто--'

# admin.site.disable_action('delete_selected')
