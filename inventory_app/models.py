import os
import uuid

from django.db import models
from django.db.models import Sum

# Create your models here.

Category = (
    ("Eyes", "Eyes"),
    ("Face", "Face"),
    ("Body Care", "Body Care"),
    ("Brushes and Beauty Blenders", "Brushes and Beauty Blenders"),
    ("Accessories", "Accessories"),
    ("Kit", "Kit"),
)


def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)
    ext = filename.split(".")[-1]
    full_name = f"{name}.{ext}"
    return os.path.join('Product', full_name)


class Product(models.Model):
    productCode = models.IntegerField()
    productName = models.CharField(max_length=50)
    productDescription = models.CharField(max_length=1000)
    productCategory = models.CharField(max_length=50, choices=Category, default="Eyes")
    # productImage = models.ImageField(upload_to=unique_img_name, null=True)
    productPrice = models.DecimalField(max_digits=5, decimal_places=0)
    productQuantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Every time an update happens

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["productCategory"]


class Supplier(models.Model):
    supplierID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    contact = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Every time an update happens

    def __str__(self):
        return self.name


# Customers
class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Every time an update happens

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('sales', 'Sales'),
        ('purchases', 'Purchases'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Every time an update happens

# Orders
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Every time an update happens


# Order Details
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Every time an update happens


class ProfitAndLoss(models.Model):
    sales = models.DecimalField(max_digits=10, decimal_places=2)
    purchases = models.DecimalField(max_digits=10, decimal_places=2)
    # expenses = models.DecimalField(max_digits=10, decimal_places=2)
    net_profit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Every time an update happens

    def calculate_net_profit(self):
        # Calculate net profit by subtracting purchases and expenses from sales
        self.net_profit = self.sales - self.purchases
        self.save()

    def __str__(self):
        return f"Profit and Loss Record - ID: {self.pk}"
