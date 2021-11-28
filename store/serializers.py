from rest_framework import serializers
from .models import Product, ShoppingCartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=100)

    # cart_items = serializers.SerializerMethodField()
    # cart_items = CartItemSerializer(read_only=True)

    price = serializers.DecimalField(
        min_value=1.00, max_value=10000000,
        max_digits=None, decimal_places=2
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end', 'is_on_sale', 'current_price')
        # depth = 1
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['is_on_sale'] = instance.is_on_sale()
    #     data['current_price'] = instance.current_price()
    #     return data

    # serializerMethodField get_ is prefix to the field name for the method that is called
    # def get_cart_items(self, instance):
    #     items = ShoppingCartItem.objects.filter(product=instance)
    #     return CartItemSerializer(items, many=True)