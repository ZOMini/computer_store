#my_project_6/main_app

from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    # path('store/', views.store_catalog),
    path('store/item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('store/item/<int:item_id>/edit/', views.item_edit, name='item_edit'),
    path('store/item/order/<int:name_id>/', views.order, name='item_order'),
    path('store/create_item/', views.item_create, name='item_create'),
    path('store/name/<int:name_id>/', views.name_detail, name='name_detail'),
    path('store/name/<int:name_id>/edit/', views.name_edit, name='name_edit'),
    path('store/create_name/', views.name_create, name='name_create'),
    path('store/category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('store/category/<int:category_id>/edit/', views.category_edit, name='category_edit'),
    path('store/create_category/', views.category_create, name='category_create'),
    path('store/all_categories/', views.all_categories, name='all_categories'),
    path('store/staff_panel/', views.staff_panel, name='staff_panel'),
    
]
