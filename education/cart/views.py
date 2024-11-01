import json

from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from mycourses.models import PurchasedCourse
from .models import Order

def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        for product_id, item in cart.items():
            quantity = item['quantity']
            price = item['price']
            total_price = quantity * price

            order = Order(product_id=product_id, quantity=quantity, total_price=total_price)
            order.save()

            purchased_course = PurchasedCourse(user=request.user, course=product_id)
            purchased_course.save()

        request.session['cart'] = {}

        return redirect('cart:success')

    return render(request, 'pages/checkout.html')


def success(request):
    return render(request, 'pages/success.html')


def load_products():
    with open(r'D:\coursemarket\products.json', 'r') as file:
        data = json.load(file)
    return data


def add_to_cart(request, product_id):
    products = load_products()
    cart = request.session.get('cart', {})

    print(f"Cart before adding: {cart}")

    product = products.get(str(product_id))
    if product:
        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += 1

        else:
            cart[str(product_id)] = {
                'quantity': 1,
                'title': product['title'],
                'price': product['price'],
            }

        request.session['cart'] = cart

    return redirect('cart:cart')


def cart(request):
    cart = request.session.get('cart', {})

    total_price = sum(item.get('quantity', 0) * item.get('price', 0) for item in cart.values())


    user_data = {}
    if request.user.is_authenticated:
        user_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'username': request.user.username,
        }

    return render(request, 'pages/cart.html', {
        'cart_items': cart,
        'total_price': total_price,
        'user_data': user_data
    })
