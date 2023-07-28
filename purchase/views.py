from django.shortcuts import render
import datetime
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db.models import Avg, Count, Min, Sum
from django.db.models.functions import TruncDate, TruncMonth
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import StandardResultsSetPagination
from .models import Supplier, Purchase, PurchaseItem
from .serializers import SupplierSerializer, PurchaseSerializer, PurchaseItemSerializer



# --------------------- SUPPLIER --------------------- 
class SupplierViewSet(viewsets.ModelViewSet):
  queryset = Supplier.objects.all().order_by('name', '-created_at')
  serializer_class = SupplierSerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['name', 'supplier_ref']
  pagination_class = StandardResultsSetPagination
  ordering_fields = ['created_at']


# --------------------- PURCHASE --------------------- 
class PurchaseViewSet(viewsets.ModelViewSet):
  queryset = Purchase.objects.prefetch_related('purchase_items').all().order_by('-created_at')
  serializer_class = PurchaseSerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['purchase_ref', 'name']
  pagination_class = StandardResultsSetPagination
  ordering_fields = ['-created_at']


# --------------------- PURCHASE ITEM --------------------- 
class PurchaseItemViewSet(viewsets.ModelViewSet):
  queryset = PurchaseItem.objects.all().order_by('-created_at')
  serializer_class = PurchaseItemSerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['product_name', 'created_at']
  pagination_class = StandardResultsSetPagination
  ordering_fields = ['-created_at']
