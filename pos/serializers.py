from django.db import transaction
from rest_framework import serializers
from .models import Currency, Sales, SalesItem
from product.models import Product
import pprint

class CurrencySerializer(serializers.ModelSerializer):
   user_id = serializers.IntegerField(allow_null=True)
   class Meta:
      model = Currency
      fields = ['id', 'name', 'rate', 'user_id']


class SalesItemSerializer(serializers.ModelSerializer):
    sales = serializers.PrimaryKeyRelatedField(read_only=True)
    product_id = serializers.IntegerField(allow_null=True)
    class Meta:
        model = SalesItem
        fields = ['id', 'sales', 'product_id', 'user_id', 'product_name', 'unit_price', 'total_price', 'quantity_sold', 'currency', 'created_at', 'updated_at']


class SalesSerializer(serializers.ModelSerializer):
    sales_items = SalesItemSerializer(many=True)
    class Meta:
        model = Sales
        fields = ['id', 'user', 'grandtotal', 'quantity_total', 'amount_paid', 'subtotal', 'tax', 'payment_method', 'change', 'owing', 'currency', 'sales_items', 'created_at', 'updated_at']

    def create(self, validated_data):
        sales_items_data = validated_data.pop('sales_items')
        sales = Sales.objects.create(**validated_data)
        for item_data in sales_items_data:
            SalesItem.objects.create(sales=sales, **item_data)
            product_id = item_data.pop('product_id')
            product = Product.objects.get(id=product_id)
            quantity_sold = item_data.pop('quantity_sold')
            quantity = product.quantity - quantity_sold
            Product.objects.filter(id=product_id).update(quantity=quantity)
        return sales


class SalesDailyUSDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['currency', 'created_at', 'quantity_total', 'grandtotal']


class SalesDailyZWLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['currency', 'created_at', 'quantity_total', 'grandtotal']


class SalesMonthlyUSDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['currency', 'created_at', 'quantity_total', 'grandtotal']


class SalesMonthlyZWLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['currency', 'created_at', 'quantity_total', 'grandtotal']


class SalesItemDailyProductUSDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesItem
        fields = ['product_name','currency', 'created_at', 'quantity_sold', 'total_price']


class SalesItemDailyProductZWLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesItem
        fields = ['product_name','currency', 'created_at', 'quantity_sold', 'total_price']