from django.urls import path
from .views import InfoView

app_name = 'main'

urlpatterns = [
    path('info/', InfoView.as_view(), name='info'),
]
