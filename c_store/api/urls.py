from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.views import (
    AltDeleteItemsSerialViews,
    CategoryViewSet,
    DeleteItemsSerialViews,
    ItemViewSet,
    NameViewSet,
    PostItemsSerialViews
)

app_name = 'api'


router_v1 = DefaultRouter()
router_v1.register('category', CategoryViewSet, 'category')
router_v1.register('item', ItemViewSet, 'item')
router_v1.register('name', NameViewSet, 'name')

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
    path('v1/post_items_serial/<name_id>/',
         PostItemsSerialViews.as_view(), name='post_items_serial'),
    path('v1/delete_items_serial/',
         DeleteItemsSerialViews.as_view(), name='delete_items_serial'),
    path('v1/alt_delete_items_serial/',
         AltDeleteItemsSerialViews.as_view(), name='alt_delete_items_serial'),
    path('v1/', include(router_v1.urls)),
]
urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] 
