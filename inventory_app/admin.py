from django.contrib import admin
from inventory_app.models import (Transaction, Product, Category, Order, OrderDetail, Customer,
                                  Supplier, ProfitAndLoss)


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productName', 'productCategory', 'productPrice']
    list_per_page = 25


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'address',)
    list_per_page = 25


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'total_amount',)
    list_filter = ('customer', 'order_date',)  # Enable filtering by customer and order date
    list_per_page = 25


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'subtotal',)
    list_filter = ('order', 'product',)  # Enable filtering by order and product
    list_per_page = 25


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'amount', 'date',)
    list_filter = ('transaction_type', 'date',)  # Enable filtering by transaction type and date
    list_per_page = 25


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'created_at')


@admin.register(ProfitAndLoss)
class ProfitAndLossAdmin(admin.ModelAdmin):
    list_display = ('sales', 'purchases', 'net_profit', 'created_at')
