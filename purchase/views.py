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
from .serializers import SupplierSerializer, PurchaseSerializer, PurchaseItemSerializer, \
      PurchaseItemDailyProductUSDSerializer, PurchaseItemDailyProductZWLSerializer, \
      PurchaseItemMonthlyProductUSDSerializer, PurchaseItemMonthlyProductZWLSerializer, \
      PurchaseDailySupplierSerializer, PurchaseMonthlySupplierSerializer, \
      PurchaseDailySerializer, \
      AllPurchaseItemByDaySerializer



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
  queryset = Purchase.objects.prefetch_related('user', 'purchase_items').all().order_by('-created_at', '-id')
  serializer_class = PurchaseSerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['purchase_ref', 'supplier_ref']
  pagination_class = StandardResultsSetPagination
  ordering_fields = ['-created_at']


# --------------------- PURCHASES DAILY --------------------- 
class PurchaseDailyUSDViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.values('currency', 'created_at').filter(currency='USD') \
        .annotate( purchase_total=Sum('purchase_total'), quantity_total=Sum('quantity_total')).order_by('-created_at', '-id')
    serializer_class = PurchaseDailySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


class PurchaseDailyZWLViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.values('currency', 'created_at').filter(currency='ZWL') \
        .annotate( purchase_total=Sum('purchase_total'), quantity_total=Sum('quantity_total')).order_by('-created_at', '-id')
    serializer_class = PurchaseDailySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


# --------------------- PURCHASE ITEM --------------------- 
class PurchaseItemViewSet(viewsets.ModelViewSet):
  queryset = PurchaseItem.objects.all().order_by('-created_at', '-id')
  serializer_class = PurchaseItemSerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['product_name', 'created_at']
  pagination_class = StandardResultsSetPagination
  ordering_fields = ['-created_at']


# --------------------- PURCHASE ITEM BOUGHT PER DAY--------------------- 
class PurchaseItemDailyProductUSDViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.values('product_name', 'currency', 'created_at').filter(currency='USD').annotate(total_cost=Sum('total_cost'), quantity_bought=Sum('quantity_bought')).order_by('-created_at')
    serializer_class = PurchaseItemDailyProductUSDSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name', 'created_at']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']

class PurchaseItemDailyProductZWLViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.values('product_name', 'currency', 'created_at').filter(currency='ZWL').annotate(total_cost=Sum('total_cost'), quantity_bought=Sum('quantity_bought')).order_by('-created_at')
    serializer_class = PurchaseItemDailyProductZWLSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name', 'created_at']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


# --------------------- PURCHASE ITEM BOUGHT PER MONTH --------------------- 
class PurchaseItemMonthlyProductUSDViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.values('created_at__month', 'created_at__year', 'product_name', 'currency').filter(currency='USD').annotate(total_cost=Sum('total_cost'), quantity_bought=Sum('quantity_bought')).order_by('-created_at__year', '-created_at__month')
    serializer_class = PurchaseItemMonthlyProductUSDSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name', 'created_at']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


class PurchaseItemMonthlyProductZWLViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.values('created_at__month', 'created_at__year', 'product_name', 'currency').filter(currency='ZWL').annotate(total_cost=Sum('total_cost'), quantity_bought=Sum('quantity_bought')).order_by('-created_at__year', '-created_at__month')
    serializer_class = PurchaseItemMonthlyProductZWLSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


# --------------------- PURCHASE ITEM BY USER --------------------- 
class PurchaseMonthlySupplierViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('-created_at')
    serializer_class = PurchaseMonthlySupplierSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        supplier_id = self.request.query_params.get('supplier_id')
        if supplier_id:
            queryset = queryset.prefetch_related('supplier').filter(supplier_id=supplier_id).values('currency', 'supplier_id', 'created_at__year', 'created_at__month').annotate(purchase_total=Sum('purchase_total'), quantity_total=Sum('quantity_total')).order_by('-created_at__year', '-created_at__month')
        return queryset


class PurchaseDailySupplierViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('-created_at')
    serializer_class = PurchaseDailySupplierSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        supplier_id = self.request.query_params.get('supplier_id')
        if supplier_id:
            queryset = queryset.filter(supplier_id=supplier_id).values('currency', 'supplier_id', 'created_at').annotate(purchase_total=Sum('purchase_total'), quantity_total=Sum('quantity_total')).order_by('-created_at')
        return queryset


# --------------------- PURCHASE ITEM BY DAY --------------------- 
class AllPurchaseItemByDayUSDViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.filter(currency='USD').order_by('product_name', '-created_at')
    serializer_class = AllPurchaseItemByDaySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at')
        if created_at:
            queryset = queryset.filter(currency='USD', created_at=created_at).values('product_id', 'product_name', 'currency', 'created_at') \
                .annotate(quantity_bought=Sum('quantity_bought'), total_cost=Sum('total_cost')).order_by('product_name')
        return queryset

# ZWL
class AllPurchaseItemByDayZWLViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.filter(currency='ZWL').order_by('product_name', '-created_at')
    serializer_class = AllPurchaseItemByDaySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at')
        if created_at:
            queryset = queryset.filter(currency='ZWL', created_at=created_at).values('product_id', 'product_name', 'currency', 'created_at') \
                .annotate(quantity_bought=Sum('quantity_bought'), total_cost=Sum('total_cost')).order_by('product_name')
        return queryset

# ---- PAGINATED ----
class AllPurchaseItemByDayPaginatedUSDViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.filter(currency='USD').order_by('product_name', '-created_at')
    serializer_class = AllPurchaseItemByDaySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at')
        if created_at:
            queryset = queryset.filter(currency='USD', created_at=created_at).values('product_id', 'product_name', 'currency', 'created_at') \
                .annotate(quantity_bought=Sum('quantity_bought'), total_cost=Sum('total_cost')).order_by('product_name')
        return queryset


class AllPurchaseItemByDayPaginatedZWLViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.filter(currency='ZWL').order_by('product_name', '-created_at')
    serializer_class = AllPurchaseItemByDaySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at')
        if created_at:
            queryset = queryset.filter(currency='ZWL', created_at=created_at).values('product_id', 'product_name', 'currency', 'created_at') \
                .annotate(quantity_bought=Sum('quantity_bought'), total_cost=Sum('total_cost')).order_by('product_name')
        return queryset











