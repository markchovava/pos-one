from django.db import models
from django.contrib.auth.models import User
from product.models import Product



# Create your models here.
class Currency(models.Model):
   name = models.CharField(max_length=255)
   rate = models.IntegerField(null=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self) -> str:
      return self.name

   class Meta:
      ordering = ['name', 'rate', 'created_at', 'updated_at']


class Sales(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   grandtotal = models.BigIntegerField(null=True, blank=True)
   amount_paid = models.BigIntegerField(null=True, blank=True)
   subtotal = models.BigIntegerField(null=True, blank=True)
   quantity_total = models.IntegerField(null=True, blank=True)
   tax = models.IntegerField(null=True, blank=True)
   change = models.BigIntegerField(null=True, blank=True)
   owing = models.BigIntegerField(null=True, blank=True)
   currency = models.CharField(max_length=255, null=True, blank=True)
   payment_method = models.CharField(max_length=255, null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self) -> str:
      return self.grandtotal

   class Meta:
      ordering = ['grandtotal', '-created_at', '-updated_at']


class SalesItem(models.Model):
   sales = models.ForeignKey(Sales, on_delete=models.CASCADE, related_name='sales_items', null=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
   product_name = models.CharField(max_length=255, null=True, blank=True)
   unit_price = models.IntegerField(null=True, blank=True)
   total_price = models.IntegerField(null=True, blank=True)
   quantity_sold = models.IntegerField(null=True, blank=True)
   currency = models.CharField(max_length=255, null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self) -> str:
      return self.product_name

   class Meta:
      ordering = ['product_name', 'quantity_sold', 'total_price', '-created_at', '-updated_at']




