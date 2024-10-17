from django.urls import path

from . import views


app_name = 'pages'

urlpatterns = [
    path('info/', views.info, name='info'),
]