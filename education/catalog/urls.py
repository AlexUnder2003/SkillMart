from django.urls import path

from . import views


app_name = 'catalog'


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:id>/', views.catalog_detail, name='catalog_detail'),
]
