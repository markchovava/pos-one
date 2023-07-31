from django.db import models
from django.conf import settings
from product.models import Product


# SUPPLIER
class Supplier(models.Model):
    supplier_ref = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
      ordering = ['name', '-created_at', '-updated_at']



class Purchase(models.Model):
    purchase_ref = models.CharField(max_length=255, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    purchase_total = models.BigIntegerField(null=True, blank=True)
    quantity_total = models.IntegerField(null=True, blank=True)
    amount_paid = models.IntegerField(null=True, blank=True)
    owing = models.IntegerField(null=True, blank=True)
    change = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    supplier_ref = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.ref_no)

    class Meta:
        ordering = ['purchase_ref', '-created_at', '-updated_at']


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase_items', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    unit_cost = models.IntegerField(null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=True)
    quantity_bought = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.product_name

    class Meta:
        ordering = ['product_name', 'quantity_bought', '-created_at', '-updated_at']



