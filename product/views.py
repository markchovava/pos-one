from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .pagination import StandardResultsSetPagination
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, EditProductSerializer, CategorySerializer, \
              ProductPriceSerializer


class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.prefetch_related('category__product').all().order_by('name')
  filter_backends = [SearchFilter]
  search_fields = ['name', 'barcode']
  ordering_fields = ['unit_price', 'updated_at']
  pagination_class = StandardResultsSetPagination

  def get_serializer_class(self):
    if self.request.method == 'POST' or self.request.method == 'PATCH' or self.request.method == 'PUT':
      return EditProductSerializer
    return ProductSerializer

class ProductStockViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all().order_by('quantity')
  serializer_class = ProductSerializer
  filter_backends = [SearchFilter]
  search_fields = ['name', 'barcode']
  ordering_fields = ['unit_price', 'updated_at']
  pagination_class = StandardResultsSetPagination


class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  filter_backends = [SearchFilter]
  search_fields = ['name']
  ordering_fields = ['name', 'updated_at']


class ProductPriceViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all().order_by('-updated_at', 'name')
  serializer_class = ProductPriceSerializer
  filter_backends = [SearchFilter]
  search_fields = ['name', 'barcode']
  pagination_class = StandardResultsSetPagination

  def update(self, request, *args, **kwargs):
    products = request.data.get('products', [])
    for product in products:
        product_id = product["id"]
        Product.objects.filter(id=product_id).update(**product)
    return Response(status=200)





