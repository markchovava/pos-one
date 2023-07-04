from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from pos.models import Sales
from pos.serializers import SalesSerializer

# Create your views here.
class UserSalesViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  @action(detail=False)
  def user_list(self, request):
    sales = Sales.objects.get(user_id=request.user.id)
    if sales is not None:
      serializer = SalesSerializer(sales)
      return Response(serializer.data)
    return Response('Is Empty.')