from django.db import transaction
from rest_framework import serializers
from .models import Supplier, Purchase, PurchaseItem
from core.models import User
from product.models import Product
from core.serializers import UserSerializer



class SupplierSerializer(serializers.ModelSerializer):
   user_id = serializers.IntegerField(allow_null=True)
   user = UserSerializer(read_only=True)

   class Meta:
      model = Supplier
      fields = ['id', 'user_id', 'supplier_ref', 'name', 'phone_number', 'address', 'email', 'user', 'created_at']


class PurchaseItemSerializer(serializers.ModelSerializer):
    purchase = serializers.PrimaryKeyRelatedField(read_only=True)
    product_id = serializers.IntegerField(allow_null=True)
    user_id = serializers.IntegerField(allow_null=True)
    class Meta:
        model = PurchaseItem
        fields = ['id', 'purchase', 'product_id', 'user_id', 'product_name', 'unit_cost', 'total_cost', 'quantity_bought', 'currency', 'created_at', 'updated_at']


class PurchaseSerializer(serializers.ModelSerializer):
    purchase_items = PurchaseItemSerializer(many=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(allow_null=True)
    supplier_id = serializers.IntegerField(allow_null=True)
    supplier = SupplierSerializer(many=False, read_only=True)
    
    class Meta:
        model = Purchase
        fields = ['id', 'user', 'user_id', 'purchase_ref', 'supplier_ref', 'supplier', 'supplier_id', 'supplier_name', 'purchase_total', 'quantity_total', 'amount_paid', 'payment_method', 'owing', 'currency', 'purchase_items', 'created_at', 'updated_at']

    def create(self, validated_data):
        purchase_items_data = validated_data.pop('purchase_items')
        purchase = Purchase.objects.create(**validated_data)
        for item_data in purchase_items_data:
            PurchaseItem.objects.create(purchase=purchase, **item_data)
            product_id = item_data.pop('product_id')
            product = Product.objects.get(id=product_id)
            quantity_bought = item_data.pop('quantity_bought')
            quantity = product.quantity + quantity_bought
            Product.objects.filter(id=product_id).update(quantity=quantity)
        return purchase 


