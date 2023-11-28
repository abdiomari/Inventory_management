from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from inventory_app.models import Product, Supplier, Customer, Transaction, Order, OrderDetail


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "productPrice": forms.NumberInput(attrs={"max": 70000, "min": 10})
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

        widgets = {
            "order_date": forms.DateInput(
                attrs={"type": "date", "min": "2022-01-01"})

        }


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
