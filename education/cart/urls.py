from django.urls import path
from .views import CartView, CheckoutView, SuccessView, AddToCartView

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('success/', SuccessView.as_view(), name='success'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
]
