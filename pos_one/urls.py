"""
URL configuration for pos_one project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from product.views import ProductViewSet, CategoryViewSet
from core.views import UserSalesViewSet
from pos.views import CurrencyViewSet, SalesViewSet, SalesItemViewSet, SalesDailyUSDViewSet, SalesDailyZWLViewSet, SalesMonthlyUSDViewSet, \
    SalesMonthlyZWLViewSet, SalesItemDailyProductUSDViewSet, SalesItemDailyProductZWLViewSet, ProductSalesItemByDayUSDViewSet, \
    ProductSalesItemByDayZWLViewSet


router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='category')
router.register('currency', CurrencyViewSet, basename='currency')
router.register('sales', SalesViewSet, basename='sales')
router.register('user/sales', UserSalesViewSet, basename='user-sales')
router.register('sales/daily/usd', SalesDailyUSDViewSet, basename='sales-daily-usd')
router.register('sales/daily/zwl', SalesDailyZWLViewSet, basename='sales-daily-zwl')
router.register('sales/monthly/usd', SalesMonthlyUSDViewSet, basename='sales-monthly-usd')
router.register('sales/monthly/zwl', SalesMonthlyZWLViewSet, basename='sales-monthly-zwl')
router.register('salesitem', SalesItemViewSet, basename='salesitem')
router.register('salesitem/daily/product/usd', SalesItemDailyProductUSDViewSet, basename='salesitem-daily-product-usd')
router.register('salesitem/daily/product/zwl', SalesItemDailyProductZWLViewSet, basename='salesitem-daily-product-zwl')
router.register('salesitem/byday/product/usd', ProductSalesItemByDayUSDViewSet, basename='salesitem-byday-product-usd')
router.register('salesitem/byday/product/zwl', ProductSalesItemByDayZWLViewSet, basename='salesitem-byday-product-zwl')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]
