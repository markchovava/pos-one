from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .pagination import StandardResultsSetPagination
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, EditProductSerializer, CategorySerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.prefetch_related('category__product').all()
  filter_backends = [SearchFilter]
  search_fields = ['name']
  ordering_fields = ['unit_price', 'updated_at']
  pagination_class = StandardResultsSetPagination

  def get_serializer_class(self):
    if self.request.method == 'POST' or self.request.method == 'PATCH' or self.request.method == 'PUT':
      return EditProductSerializer
    return ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  filter_backends = [SearchFilter]
  search_fields = ['name']
  ordering_fields = ['name', 'updated_at']



