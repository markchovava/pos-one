from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from .models import User

# Create your views here.
class UserAllViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserAllSerializer
