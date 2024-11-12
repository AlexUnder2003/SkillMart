import json

from django.shortcuts import render, redirect

from mycourses.models import PurchasedCourse
from .forms import CheckoutForm
from .models import Order


def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        # Заполняем форму данными из POST-запроса
        form = CheckoutForm(request.POST)

        if form.is_valid():
            # Извлекаем данные из формы
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data.get('username', request.user.username if request.user.is_authenticated else '')

            print(first_name)
            # Создаём заказы для каждого товара в корзине
            for product_id, item in cart.items():
                quantity = item['quantity']
                price = item['price']
                total_price = quantity * price

                order = Order(
                    user=request.user if request.user.is_authenticated else None,
                    product_id=product_id,
                    quantity=quantity,
                    total_price=total_price,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                order.save()

                # Сохраняем информацию о приобретённых курсах
                purchased_course = PurchasedCourse(user=request.user, course=product_id)
                purchased_course.save()

            # Очищаем корзину после успешного оформления заказа
            request.session['cart'] = {}

            return redirect('cart:success')
        else:
            # Если форма не прошла валидацию, вернём страницу с ошибками
            print('Form is not valid')
            print(form.errors)
            return render(request, 'pages/cart.html', {
                'form': form,
                'cart_items': cart,
                'total_price': sum(item.get('quantity', 0) * item.get('price', 0) for item in cart.values())
            })

    # GET-запрос: отображаем форму для ввода данных
    else:
        form = CheckoutForm()
        return render(request, 'pages/cart.html', {
            'form': form,
            'cart_items': cart,
            'total_price': sum(item.get('quantity', 0) * item.get('price', 0) for item in cart.values())
        })



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

    user_data = {}

    if request.user.is_authenticated:
        user_data = {
            'email': request.user.email,
            'username': request.user.username,
        }

    form = CheckoutForm(initial=user_data)

    total_price = sum(item.get('quantity', 0) * item.get('price', 0) for item in cart.values())

    return render(request, 'pages/cart.html', {
        'cart_items': cart,
        'total_price': total_price,
        'form': form
    })
