from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework import serializers

from inventory_app.models import Product, OrderDetail


class SerializeProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SerializeOrders(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
