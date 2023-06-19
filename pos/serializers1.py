from django.db import transaction
from rest_framework import serializers
from .models import Currency, Sales, SalesItem

class CurrencySerializer(serializers.ModelSerializer):
   user_id = serializers.IntegerField(allow_null=True)
   class Meta:
      model = Currency
      fields = ['id', 'name', 'rate', 'user_id']


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class SalesItemSerializer(serializers.ModelSerializer):
    #sales = serializers.PrimaryKeyRelatedField(queryset=Sales.objects.all())
    class Meta:
        model = SalesItem
        fields = '__all__'