from rest_framework import serializers

from applications.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'link', 'quantity', 'price', 'provider']
