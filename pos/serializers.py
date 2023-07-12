from django.db import transaction
from rest_framework import serializers
from .models import Currency, Sales, SalesItem
from core.models import User
from product.models import Product
from core.serializers import UserSerializer



class CurrencySerializer(serializers.ModelSerializer):
   user_id = serializers.IntegerField(allow_null=True)
   class Meta:
      model = Currency
      fields = ['id', 'name', 'rate', 'user_id']


class SalesItemSerializer(serializers.ModelSerializer):
    sales = serializers.PrimaryKeyRelatedField(read_only=True)
    product_id = serializers.IntegerField(allow_null=True)
    user_id = serializers.IntegerField(allow_null=True)
    class Meta:
        model = SalesItem
        fields = ['id', 'sales', 'product_id', 'user_id', 'product_name', 'unit_price', 'total_price', 'quantity_sold', 'currency', 'created_at', 'updated_at']


class SalesSerializer(serializers.ModelSerializer):
    sales_items = SalesItemSerializer(many=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(allow_null=True)
    class Meta:
        model = Sales
        fields = ['id', 'user', 'user_id', 'ref_no', 'grandtotal', 'quantity_total', 'amount_paid', 'subtotal', 'tax', 'payment_method', 'change', 'owing', 'currency', 'sales_items', 'created_at', 'updated_at']

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


""" --------------------------DAY--------------------- """

class SalesDailyUSDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['currency', 'created_at', 'quantity_total', 'grandtotal']


class SalesDailyZWLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['currency', 'created_at', 'quantity_total', 'grandtotal']


class SalesItemDailyProductUSDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesItem
        fields = ['product_name', 'currency', 'created_at', 'quantity_sold', 'total_price']


class SalesItemDailyProductZWLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesItem
        fields = ['product_name','currency', 'created_at', 'quantity_sold', 'total_price']


class ProductSalesItemByDayUSDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesItem
        fields = ['product_name', 'currency', 'created_at', 'quantity_sold', 'total_price']


class ProductSalesItemByDayZWLSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesItem
        fields = ['product_name', 'currency', 'created_at', 'quantity_sold', 'total_price']



""" --------------------------MONTH--------------------- """

class SalesMonthlyUSDListSerializer(serializers.ModelSerializer):
    month = serializers.IntegerField(source='created_at__month')
    year = serializers.IntegerField(source='created_at__year')
    class Meta:
        model = Sales
        fields = ['currency', 'month', 'year', 'created_at', 'quantity_total', 'grandtotal']


class SalesMonthlyZWLListSerializer(serializers.ModelSerializer):
    month = serializers.IntegerField(source='created_at__month')
    year = serializers.IntegerField(source='created_at__year')
    class Meta:
        model = Sales
        fields = ['currency', 'month', 'year', 'created_at', 'quantity_total', 'grandtotal']


class ProductSalesItemMonthlyUSDSerializer(serializers.ModelSerializer):
    month = serializers.IntegerField(source='created_at__month')
    year = serializers.IntegerField(source='created_at__year')
    class Meta:
        model = SalesItem
        fields = ['product_name', 'currency', 'month', 'year', 'quantity_sold', 'total_price']


class ProductSalesItemMonthlyZWLSerializer(serializers.ModelSerializer):
    month = serializers.IntegerField(source='created_at__month')
    year = serializers.IntegerField(source='created_at__year')
    class Meta:
        model = SalesItem
        fields = ['product_name', 'currency', 'month', 'year', 'quantity_sold', 'total_price']


class UserMonthlySalesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    month = serializers.IntegerField(source='created_at__month')
    year = serializers.IntegerField(source='created_at__year')

    def get_user(self, obj):
        user_id = obj.user_id
        user = User.objects.get(pk=user_id)
        return user
  
    class Meta:
        model = Sales
        fields = ['created_at', 'user', 'user_id', 'currency', 'month', 'year', 'quantity_total', 'grandtotal']


class UserDailySalesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    def get_user(self, obj):
        user_id = obj.user_id
        user = User.objects.get(pk=user_id)
        return user
  
    class Meta:
        model = Sales
        fields = ['created_at', 'user', 'user_id', 'currency', 'quantity_total', 'grandtotal']

    
""" -------------------------- USER SALES --------------------- """
class SalesAllByUserSerializer(serializers.ModelSerializer):
    sales_items = SalesItemSerializer(many=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(allow_null=True)
    class Meta:
        model = Sales
        fields = ['id', 'user', 'user_id', 'ref_no', 'grandtotal', 'quantity_total', 'currency', 'sales_items', 'created_at' ] 


class SalesLatestByUserSerializer(serializers.ModelSerializer):
    sales_items = SalesItemSerializer(many=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(allow_null=True)
    class Meta:
        model = Sales
        fields = ['id', 'user', 'user_id', 'ref_no', 'grandtotal', 'quantity_total', 'currency', 'sales_items', 'created_at' ] 

   
  
       
