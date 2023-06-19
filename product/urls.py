from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
# from pprint import pprint

# router = routers.DefaultRouter()
# router.register('product', views.ProductViewSet, basename='product')
# router.register('category', views.CategoryViewSet, basename='category')
# router.register('brand', views.BrandViewSet, basename='brand')
# pprint(router.urls)

# urlpatterns = [
#    path('', include(router.urls)),
# ]