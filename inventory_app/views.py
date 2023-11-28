from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.renderers import JSONRenderer

from inventory_app.app_forms import ProductForm, CustomerForm, OrderForm, TransactionForm, \
    OrderDetailForm, SupplierForm, LoginForm, SignUpForm
from inventory_app.models import Product, Customer, OrderDetail, Transaction, Supplier
from inventory_app.serializer import SerializeProducts, SerializeOrders


# Create your views here

def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)

    orders = OrderDetail.objects.all()
    customers = Customer.objects.all()
    transactions = Transaction.objects.all()
    suppliers = Supplier.objects.all()

    context = {
        'products': data,
        'orders': orders,
        'customers': customers,
        'transactions': transactions,
        'suppliers': suppliers,
    }

    return render(request, "index.html", context)


def sales(request):
    return render(request, "sales.html")


def purchases(request):
    return render(request, "purchases.html")


def add_customers(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Added new Product")
            return redirect("home")
    else:
        form = CustomerForm()
    return render(request, "add_customer.html", {"form": form})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Added new Product")
            return redirect("home")
    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})


def view_customers(request):
    customers = Customer.objects.all()
    paginator = Paginator(customers, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, "view_customers.html", {"customers": customers})


def view_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, "view_products.html", {"products": data})


def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Added new Product")
            return redirect("home")
    else:
        form = OrderForm()
    return render(request, "add_order.html", {"form": form})


def view_orders(request):
    orders = OrderDetail.objects.all()
    paginator = Paginator(orders, 5)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, "index.html", {"products": data})


def add_transactions(request):
    if request.method == "POST":
        form = TransactionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Added new Product")
            return redirect("home")
    else:
        form = TransactionForm()
    return render(request, "add_transaction.html", {"form": form})


def view_transactions(request):
    transactions = Transaction.objects.all()
    paginator = Paginator(transactions, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, "view_transactions.html", {"products": data})


def add_order_details(request):
    if request.method == "POST":
        form = OrderDetailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Added new Product")
            return redirect("home")
    else:
        form = OrderDetailForm()
    return render(request, "add_order_details.html", {"form": form})


def view_order(request, prod_id):
    product = Product.objects.get(pk=prod_id)
    return render(request, "view_order_details.html", {"product": product})


# def product_delete(request, prod_id):
#     product = get_object_or_404(Product, pk=prod_id)
#     product.delete()
#     messages.warning(request, "This employee was deleted permanently")
#     return redirect("all")
#

def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "signin.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        messages.error(request, "Wrong username or password")
        return render(request, "signin.html", {"form": form})


# python man


def signout(request):
    logout(request)
    return redirect('signin')


def product_details(request, prod_id):
    product = Product.objects.get(pk=prod_id)
    return render(request, "view_product.html", {"product": product})


def delete_product(request, prod_id):
    product = get_object_or_404(Product, pk=prod_id)
    product.delete()
    messages.warning(request, "This product was deleted permanently")
    return redirect("home")


def update_products(request, prod_id):
    product = get_object_or_404(Product, pk=prod_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully")
            return redirect('product_details', prod_id)
    else:
        form = ProductForm(instance=product)
    return render(request, "update_product.html", {"form": form})


def add_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Added new Supplier")
            return redirect("home")
    else:
        form = SupplierForm()
    return render(request, "add_supplier.html", {"form": form})


def view_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "view_suppliers.html", {"suppliers": suppliers})


def view_order_details(request):
    order_details = OrderDetail.objects.all()
    return render(request, "view_order_details.html", {"suppliers": order_details})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {"form": form})

