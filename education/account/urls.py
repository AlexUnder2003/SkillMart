from django.urls import path

from . import views


app_name = 'account'

urlpatterns = [
    path('my-account/', views.my_account, name='my_account'),
    path('logout/', views.logout_user, name='logout'),
    path('update/', views.update_account, name='update'),
]
