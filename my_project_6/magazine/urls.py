#my_project_6/main_app

from django.urls import path

from magazine import views

app_name = 'magazine'

urlpatterns = [
    path('', views.index, name='index'),
    # path('magazine/', views.magazine_catalog),
    path('magazine/item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('magazine/item/<int:item_id>/edit/', views.item_edit, name='item_edit'),
    path('magazine/item/order/<int:name_id>/', views.order, name='item_order'),
    path('magazine/create_item/', views.item_create, name='item_create'),
    path('magazine/name/<int:name_id>/', views.name_detail, name='name_detail'),
    path('magazine/name/<int:name_id>/edit/', views.name_edit, name='name_edit'),
    path('magazine/create_name/', views.name_create, name='name_create'),
    path('magazine/category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('magazine/category/<int:category_id>/edit/', views.category_edit, name='category_edit'),
    path('magazine/create_category/', views.category_create, name='category_create'),
]
