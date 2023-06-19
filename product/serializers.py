from django.db import transaction
from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
   user_id = serializers.IntegerField( allow_null=True)
   class Meta:
      model = Category
      fields = ['id', 'name', 'user_id']


class ProductSerializer(serializers.ModelSerializer):
   user_id = serializers.IntegerField(allow_null=True)
   category = CategorySerializer(read_only=True)

   class Meta:
      model = Product
      fields = ['id', 'name', 'description', 'barcode', 'unit_price', 'quantity', 'category', 'brand', 'user_id']


class EditProductSerializer(serializers.ModelSerializer):
   user_id = serializers.IntegerField(allow_null=True, required=False)
   category_id = serializers.IntegerField(allow_null=True, required=False)
   # category = CategorySerializer(many=True, required=False)

   class Meta:
      model = Product
      fields = ['id', 'name', 'description', 'barcode', 'unit_price', 'quantity', 'brand', 'category_id', 'user_id']
