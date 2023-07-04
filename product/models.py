from django.conf import settings
from django.db import models


class Category(models.Model):
   name = models.CharField(max_length=255)
   description = models.TextField(null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
   def __str__(self) -> str:
      return self.name
   class Meta:
      ordering = ['name', 'created_at', 'updated_at']


class Product(models.Model):
   name = models.CharField(max_length=255)
   description = models.TextField(null=True, blank=True)
   brand = models.CharField(max_length=255, null=True, blank=True)
   barcode = models.BigIntegerField(null=True, blank=True)
   unit_price = models.IntegerField(null=True, blank=True)
   quantity = models.IntegerField(null=True, blank=True)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
   def __str__(self) -> str:
      return self.name
   class Meta:
      ordering = ['name', 'created_at', 'updated_at']




