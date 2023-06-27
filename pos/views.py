from django.shortcuts import render
from rest_framework.filters import SearchFilter
from django.db.models import Avg, Count, Min, Sum
from django.db.models.functions import TruncDate
import datetime
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .models import Currency, Sales, SalesItem
from .pagination import StandardResultsSetPagination
from .serializers import CurrencySerializer, SalesSerializer, SalesItemSerializer, SalesDailyUSDListSerializer, \
    SalesDailyZWLListSerializer, SalesMonthlyUSDListSerializer, SalesMonthlyZWLListSerializer, \
    SalesItemDailyProductUSDListSerializer, SalesItemDailyProductZWLListSerializer


# Create your views here.
class CurrencyViewSet(viewsets.ModelViewSet):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer
  filter_backends = [SearchFilter]
  search_fields = ['name']
  ordering_fields = ['name', 'updated_at']


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.prefetch_related('sales_items').all()
    serializer_class = SalesSerializer
 

class SalesItemViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.all()
    serializer_class = SalesItemSerializer
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination


class SalesDailyUSDViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.raw("SELECT id, DATE(created_at) AS date, currency, SUM(grandtotal) AS grandtotal, SUM(quantity_total) AS quantity_total FROM pos_sales WHERE currency='USD' GROUP BY date ORDER BY date DESC;")
    serializer_class = SalesDailyUSDListSerializer
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination


class SalesDailyZWLViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.raw("SELECT id, DATE(created_at) AS date, currency, SUM(grandtotal) AS grandtotal, SUM(quantity_total) AS quantity_total FROM pos_sales WHERE currency='ZWL' GROUP BY date ORDER BY date DESC;")
    serializer_class = SalesDailyZWLListSerializer
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination


class SalesMonthlyUSDViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.raw("SELECT id, MONTH(created_at) AS date, currency, SUM(grandtotal) AS grandtotal, SUM(quantity_total) AS quantity_total FROM pos_sales WHERE currency='USD' GROUP BY date ORDER BY date DESC;")
    serializer_class = SalesMonthlyUSDListSerializer
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination


class SalesMonthlyZWLViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.raw("SELECT id, MONTH(created_at) AS date, currency, SUM(grandtotal) AS grandtotal, SUM(quantity_total) AS quantity_total FROM pos_sales WHERE currency='ZWL' GROUP BY date ORDER BY date DESC;")
    serializer_class = SalesMonthlyUSDListSerializer
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination


class SalesItemDailyProductUSDViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.raw("SELECT id, product_name, DATE(created_at) AS date, currency, SUM(total_price) AS total_price, SUM(quantity_sold) AS quantity_sold FROM pos_salesitem WHERE currency='USD' GROUP BY date, product_name ORDER BY date DESC;")
    serializer_class = SalesItemDailyProductUSDListSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination


class SalesItemDailyProductZWLViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.raw("SELECT id, product_name, DATE(created_at) AS date, currency, SUM(total_price) AS total_price, SUM(quantity_sold) AS quantity_sold FROM pos_salesitem WHERE currency='ZWL' GROUP BY date, product_name ORDER BY date DESC;")
    serializer_class = SalesItemDailyProductZWLListSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination

    