from django.contrib import admin

from magazine.models import Category, Item, Name


@admin.register(Item)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'category',
        'price',
        'pub_date',
        'author',
        'serial_num',
        'status',
    )
    # list_editable = ('category','price')
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '--Пусто--'
    list_select_related = ('author', 'category',)


    # def group_1(self, request, queryset):
    #     queryset.update(group='1')
    # group_1.short_description = 'all_group_1'

    # def group_2(self, request, queryset):
    #     queryset.update(group='2')
    # group_2.short_description = 'all_group_2'

    # def group_3(self, request, queryset):
    #     queryset.update(group='3')
    # group_3.short_description = 'all_group_3'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    empty_value_display = '--Пусто--'

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('mod_name', 'mod_detail')
    search_fields = ('mod_name',)
    empty_value_display = '--Пусто--'

admin.site.disable_action('delete_selected')
