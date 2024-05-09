from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'product_type', 'product_id', 'quantity', 'subtotal']
        read_only_fields = ['id', 'subtotal']

    def get_subtotal(self, obj):
        price = self.context.get('price', 0)
        quantity = obj.quantity
        return price * quantity

    def create(self, validated_data):
        validated_data.pop('subtotal', 0)
        cart_item = Cart.objects.create(**validated_data)
        return cart_item
