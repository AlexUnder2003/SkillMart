from django.urls import path
from .views import MyAccountView, UpdateAccountView, LogoutUserView

app_name = 'account'

urlpatterns = [
    path('my_account/', MyAccountView.as_view(), name='my_account'),
    path('update_account/', UpdateAccountView.as_view(), name='update_account'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
