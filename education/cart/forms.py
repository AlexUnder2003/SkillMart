from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )

    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com', 'class': 'form-control'}),
        }

