from django.shortcuts import render
import datetime
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db.models import Avg, Count, Min, Sum
from django.db.models.functions import TruncDate, TruncMonth
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import StandardResultsSetPagination
from .models import Currency, Sales, SalesItem
from .serializers import CurrencySerializer, SalesSerializer, SalesItemSerializer, SalesDailyUSDListSerializer, SalesDailyZWLListSerializer, \
    SalesMonthlyUSDListSerializer, SalesMonthlyZWLListSerializer, SalesItemDailyProductUSDListSerializer, SalesItemDailyProductZWLListSerializer, \
    ProductSalesItemByDayUSDSerializer, ProductSalesItemByDayZWLSerializer, ProductSalesItemMonthlyUSDSerializer, ProductSalesItemMonthlyZWLSerializer, \
    UserMonthlySalesSerializer, UserDailySalesSerializer, SalesAllByUserSerializer, SalesLatestByUserSerializer


""" ---------------------------- CURRENCY ----------------------- """
class CurrencyViewSet(viewsets.ModelViewSet):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['name']
  ordering_fields = ['created_at']


""" ---------------------------- SALES ------------------------- """

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.prefetch_related('sales_items').all()
    serializer_class = SalesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']
 

class SalesItemViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.all()
    serializer_class = SalesItemSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


""" ---------------------------- DAILY ------------------------- """
class SalesDailyUSDViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.values('currency', 'created_at').filter(currency='USD').annotate( grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total'))
    serializer_class = SalesDailyUSDListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


class SalesDailyZWLViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.values('currency', 'created_at').filter(currency='ZWL').annotate( grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total'))
    serializer_class = SalesDailyZWLListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


class SalesItemDailyProductUSDViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.values('product_name', 'currency', 'created_at').filter(currency='USD').annotate(total_price=Sum('total_price'), quantity_sold=Sum('quantity_sold'))
    serializer_class = SalesItemDailyProductUSDListSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name']
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at', 'product_name']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at', 'product_name']


class SalesItemDailyProductZWLViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.values('product_name', 'currency', 'created_at').filter(currency='ZWL').annotate(total_price=Sum('total_price'), quantity_sold=Sum('quantity_sold'))
    serializer_class = SalesItemDailyProductZWLListSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at', 'product_name']


""" ---------------------------- MONTHLY ----------------------- """
class SalesMonthlyUSDViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.values('currency', 'created_at__month', 'created_at__year').filter(currency='USD').annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total'))
    serializer_class = SalesMonthlyUSDListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


class SalesMonthlyZWLViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.values('currency', 'created_at__month', 'created_at__year').filter(currency='ZWL').annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total'))
    serializer_class = SalesMonthlyZWLListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at', 'product_name']


class ProductSalesItemMonthlyUSDViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.values('product_name', 'currency', 'created_at__month', 'created_at__year').filter(currency='USD').annotate(total_price=Sum('total_price'), quantity_sold=Sum('quantity_sold'))
    serializer_class = ProductSalesItemMonthlyUSDSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at', 'product_name']


class ProductSalesItemMonthlyZWLViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.values('product_name', 'currency', 'created_at__month', 'created_at__year').filter(currency='ZWL').annotate(total_price=Sum('total_price'), quantity_sold=Sum('quantity_sold'))
    serializer_class = ProductSalesItemMonthlyZWLSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at', 'product_name']
        

class UserMonthlySalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = UserMonthlySalesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id).values('currency', 'user_id', 'created_at__month', 'created_at__year').annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total'))
        return queryset


class UserDailySalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = UserDailySalesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id).values('currency', 'user_id', 'created_at').annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total'))
        return queryset



""" -------------------------------------------------------------- """
class SalesAllByUserViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.prefetch_related('sales_items').all()
    serializer_class = SalesAllByUserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            user_id = self.request.query_params.get('user_id')
            queryset = queryset.filter(user_id=user_id)
        return queryset


class SalesLatestByUserViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.prefetch_related('sales_items').all().order_by('-created_at')
    serializer_class = SalesLatestByUserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset[:1]
   










    