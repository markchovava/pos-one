from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .models import Currency, Sales, SalesItem
from .serializers import CurrencySerializer, SalesSerializer, SalesItemSerializer

# Create your views here.
class CurrencyViewSet(viewsets.ModelViewSet):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer
  filter_backends = [SearchFilter]
  search_fields = ['name']
  ordering_fields = ['name', 'updated_at']


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    #def create(self, request):
    #    sales_serializer = SalesSerializer(data=request.data)
    #    sales_serializer.is_valid(raise_exception=True)
    #    sales = sales_serializer.save()
    #    print(sales)
    #    if request.data['sales_items']:
    #        for item in request.data['sales_items']:
    #            sales_item = SalesItemSerializer(data=item)
    #            sales_item.is_valid(raise_exception=True)
    #            sales_item.save(sales=sales)

    #    return Response(serializer.data, status=201)


    

class SalesItemViewSet(viewsets.ModelViewSet):
    queryset = SalesItem.objects.all()
    serializer_class = SalesItemSerializer
