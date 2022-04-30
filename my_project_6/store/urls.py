#my_project_6/main_app

from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from store import views

app_name = 'store'

schema_view = get_schema_view(
   openapi.Info(
      title="Store API",
      default_version='v1',
      description="Документация для приложения store проекта Store",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="ee@ya.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', 
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
       name='schema-redoc'),
] 
