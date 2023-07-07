from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from .models import User
from .serializers import UserAllSerializer
from .pagination import StandardResultsSetPagination

# Create your views here.
class UserAllViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserAllSerializer
  filter_backends = [SearchFilter]
  search_fields = ['username', 'first_name', 'last_name']
  pagination_class = StandardResultsSetPagination
