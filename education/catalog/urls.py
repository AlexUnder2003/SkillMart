from django.urls import path
from .views import CatalogView, CatalogDetailView

app_name = 'catalog'

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('<int:id>/', CatalogDetailView.as_view(), name='catalog_detail'),
]
