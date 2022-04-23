#my_project_6/main_app

from django.urls import path

from magazine import views

app_name = 'magazine'

urlpatterns = [
    path('', views.index, name='index'),
    # path('magazine/', views.magazine_catalog),
    # path('magazine/<int:pk>/', views.item_detail),
]
