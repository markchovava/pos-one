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
    UserMonthlySalesSerializer, UserDailySalesSerializer, SalesAllByUserSerializer, SalesLatestByUserSerializer, CurrentUserSalesDailySerializer, \
    CurrentUserSalesMonthlySerializer, AllSalesItemByDaySerializer


""" ---------------------------- CURRENCY ----------------------- """
class CurrencyViewSet(viewsets.ModelViewSet):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['name']
  ordering_fields = ['created_at']


""" ---------------------------- SALES ------------------------- """
class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.prefetch_related('sales_items').all().order_by('-created_at')
    serializer_class = SalesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['ref_no']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']
 

class SalesItemViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.all().order_by('-created_at')
    serializer_class = SalesItemSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['product_name', 'created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


# ---------------------------- DAILY ------------------------- """
class SalesDailyUSDViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.values('currency', 'created_at').filter(currency='USD').annotate( grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total')).order_by('-created_at')
    serializer_class = SalesDailyUSDListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


class SalesDailyZWLViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.values('currency', 'created_at').filter(currency='ZWL').annotate( grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total')).order_by('-created_at')
    serializer_class = SalesDailyZWLListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


class SalesItemDailyProductUSDViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.values('product_name', 'currency', 'created_at').filter(currency='USD').annotate(total_price=Sum('total_price'), quantity_sold=Sum('quantity_sold')).order_by('-created_at')
    serializer_class = SalesItemDailyProductUSDListSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name']
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at', 'product_name']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


class SalesItemDailyProductZWLViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.values('product_name', 'currency', 'created_at').filter(currency='ZWL').annotate(total_price=Sum('total_price'), quantity_sold=Sum('quantity_sold')).order_by('-created_at')
    serializer_class = SalesItemDailyProductZWLListSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']


# """ ---------------------------- MONTHLY ----------------------- """
class SalesMonthlyUSDViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.values('currency', 'created_at__month', 'created_at__year').filter(currency='USD').annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total')).order_by('-created_at__month', '-created_at__year')
    serializer_class = SalesMonthlyUSDListSerializer
    http_method_names = ['get', 'head', 'options']
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at__month', '-created_at__year']


class SalesMonthlyZWLViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.values('currency', 'created_at__month', 'created_at__year').filter(currency='ZWL').annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total')).order_by('-created_at__month', '-created_at__year')
    serializer_class = SalesMonthlyZWLListSerializer
    http_method_names = ['get', 'head', 'options']
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['created_at']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['created_at__month', 'created_at__year']


class ProductSalesItemMonthlyUSDViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.values('product_name', 'currency', 'created_at__month', 'created_at__year').filter(currency='USD').annotate(total_price=Sum('total_price'), quantity_sold=Sum('quantity_sold')).order_by('-created_at__month', '-created_at__year')
    serializer_class = ProductSalesItemMonthlyUSDSerializer
    http_method_names = ['get', 'head', 'options']
    search_fields = ['product_name']
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at', 'product_name']


class ProductSalesItemMonthlyZWLViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.values('product_name', 'currency', 'created_at__month', 'created_at__year').filter(currency='ZWL').annotate(total_price=Sum('total_price'), quantity_sold=Sum('quantity_sold')).order_by('-created_at__month', '-created_at__year')
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
            queryset = queryset.filter(user_id=user_id).values('currency', 'user_id', 'created_at__month', 'created_at__year').annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total')).order_by('-created_at__month', '-created_at__year')
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
            queryset = queryset.filter(user_id=user_id).values('currency', 'user_id', 'created_at').annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total')).order_by('-created_at')
        return queryset



""" -------------------------USER ------------------------------------- """
class SalesAllByUserViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.prefetch_related('sales_items').all().order_by('-created_at')
    serializer_class = SalesAllByUserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['ref_no']
    pagination_class = StandardResultsSetPagination
    ordering_fields = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id).order_by('-created_at')
        return queryset


class SalesLatestByUserViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.prefetch_related('sales_items').all().order_by('-created_at')
    serializer_class = SalesLatestByUserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.prefetch_related('sales_items').filter(user_id=user_id).order_by('-created_at')
        return queryset[:1]


""" ------------------------- CURRENT USER ------------------------------------- """
class CurrentUserSalesDailyViewset(viewsets.ModelViewSet):
    queryset = Sales.objects.prefetch_related('sales_items').all()
    serializer_class = CurrentUserSalesDailySerializer
    http_method_names = ['get', 'head', 'options']
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            # DAILY REPORT
            queryset = queryset.filter(user_id=user_id) \
                        .values('created_at', 'currency', 'user_id') \
                        .annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total')) \
                        .order_by('-created_at')
        return queryset


class CurrentUserSalesMonthlyViewset(viewsets.ModelViewSet):
    queryset = Sales.objects.prefetch_related('sales_items').all()
    serializer_class = CurrentUserSalesMonthlySerializer
    http_method_names = ['get', 'head', 'options']
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            # MONTHLY REPORT
            queryset = queryset.filter(user_id=user_id) \
                        .values('created_at__month', 'created_at__year', 'currency', 'user_id') \
                        .annotate(grandtotal=Sum('grandtotal'), quantity_total=Sum('quantity_total')) \
                        .order_by( '-created_at__year', '-created_at__month' )
        return queryset        


# ---------------------------- ALL SALES BY DAY ----------------------------------------------------------- 
class AllSalesItemByDayUSDViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.all().order_by('product_name', '-created_at')
    serializer_class = AllSalesItemByDaySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at')
        if created_at:
            queryset = queryset.filter(currency='USD', created_at=created_at).values('product_id', 'product_name', 'currency', 'created_at') \
                .annotate(quantity_sold=Sum('quantity_sold'), total_price=Sum('total_price')).order_by('product_name')
        return queryset

""" 
['product_id', 'product_name', 'currency', 'created_at', 'quantity_sold', 'total_price']
 """

class AllSalesItemByDayZWLViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.all().order_by('product_name', '-created_at')
    serializer_class = AllSalesItemByDaySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at')
        if created_at:
            queryset = queryset.filter(currency='ZWL', created_at=created_at).values('product_id', 'product_name', 'currency', 'created_at') \
                .annotate(quantity_sold=Sum('quantity_sold'), total_price=Sum('total_price')).order_by('product_name')
        return queryset


class AllSalesItemByDayPaginatedUSDViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.all().order_by('product_name', '-created_at')
    serializer_class = AllSalesItemByDaySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at')
        if created_at:
            queryset = queryset.filter(currency='USD', created_at=created_at).values('product_id', 'product_name', 'currency', 'created_at') \
                .annotate(quantity_sold=Sum('quantity_sold'), total_price=Sum('total_price')).order_by('product_name')
        return queryset


class AllSalesItemByDayPaginatedZWLViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.all().order_by('product_name', '-created_at')
    serializer_class = AllSalesItemByDaySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at')
        if created_at:
            queryset = queryset.filter(currency='ZWL', created_at=created_at).values('product_id', 'product_name', 'currency', 'created_at') \
                .annotate(quantity_sold=Sum('quantity_sold'), total_price=Sum('total_price')).order_by('product_name')
        return queryset









    