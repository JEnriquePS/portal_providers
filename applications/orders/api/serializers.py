from rest_framework import serializers
from applications.orders.models import Order
from applications.products.api.serializers import ProductSerializer
from applications.products.models import Product


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'products', 'total_price', 'request_placer', 'request_approver', 'approved']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        total_price = 0
        for product_data in products_data:
            Product.objects.create(order=order, **product_data)
            total_price += product_data['price'] * product_data['quantity']
        order.total_price = total_price
        order.save()
        return order


