from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    first_name = forms.CharField(label="Ім’я", max_length=50)
    last_name = forms.CharField(label="Прізвище", max_length=50)
    phone = forms.CharField(label="Телефон", max_length=20)
    email = forms.EmailField(label="Електронна пошта")
    address = forms.CharField(label="Адреса доставки", widget=forms.Textarea)

    delivery_method = forms.ChoiceField(
        label="Спосіб доставки",
        choices=Order.DELIVERY_CHOICES,
        widget=forms.RadioSelect
    )
    payment_method = forms.ChoiceField(
        label="Спосіб оплати",
        choices=Order.PAYMENT_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'phone', 'email',
            'address', 'delivery_method', 'payment_method'
        ]