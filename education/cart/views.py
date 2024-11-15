import json
from django.views.generic import TemplateView, FormView, View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from mycourses.models import PurchasedCourse
from .forms import CheckoutForm
from .models import Order


class CartView(TemplateView):
    template_name = 'pages/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        total_price = sum(item.get('quantity', 0) * item.get('price', 0) for item in cart.values())

        user_data = {}
        if self.request.user.is_authenticated:
            user_data = {
                'email': self.request.user.email,
                'username': self.request.user.username,
            }

        form = CheckoutForm(initial=user_data)
        context.update({
            'cart_items': cart,
            'total_price': total_price,
            'form': form,
        })
        return context


class CheckoutView(FormView):
    template_name = 'pages/cart.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('cart:success')

    def form_valid(self, form):
        cart = self.request.session.get('cart', {})
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = form.cleaned_data.get('username', self.request.user.username if self.request.user.is_authenticated else '')

        for product_id, item in cart.items():
            quantity = item['quantity']
            price = item['price']
            total_price = quantity * price

            order = Order(
                user=self.request.user if self.request.user.is_authenticated else None,
                product_id=product_id,
                quantity=quantity,
                total_price=total_price,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            order.save()

            purchased_course = PurchasedCourse(user=self.request.user, course=product_id)
            purchased_course.save()

        self.request.session['cart'] = {}
        return super().form_valid(form)

    def form_invalid(self, form):
        cart = self.request.session.get('cart', {})
        total_price = sum(item.get('quantity', 0) * item.get('price', 0) for item in cart.values())
        return self.render_to_response(self.get_context_data(form=form, cart_items=cart, total_price=total_price))


class SuccessView(TemplateView):
    template_name = 'pages/success.html'


class AddToCartView(View):
    def post(self, request, product_id):
        products = self.load_products()
        cart = request.session.get('cart', {})
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

    @staticmethod
    def load_products():
        with open(r'D:\coursemarket\products.json', 'r') as file:
            return json.load(file)
