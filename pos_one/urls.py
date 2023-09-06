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
# --------------------- PRODUCT --------------------- 
from product.views import ProductViewSet, ProductStockViewSet, CategoryViewSet, ProductPriceViewSet
# --------------------- PURCHASE --------------------- 
from purchase.views import SupplierViewSet, PurchaseItemViewSet, PurchaseViewSet, PurchaseItemDailyProductUSDViewSet, \
    PurchaseItemDailyProductZWLViewSet, PurchaseItemMonthlyProductUSDViewSet, PurchaseItemMonthlyProductZWLViewSet, \
    PurchaseMonthlySupplierViewSet, PurchaseDailySupplierViewSet, \
    PurchaseDailyUSDViewSet, PurchaseDailyZWLViewSet, \
    AllPurchaseItemByDayUSDViewSet, AllPurchaseItemByDayZWLViewSet, AllPurchaseItemByDayPaginatedUSDViewSet, AllPurchaseItemByDayPaginatedZWLViewSet
# --------------------- CORE --------------------- 
from core.views import UserAllViewSet, AppInfoViewSet
# --------------------- POINT OF SALE --------------------- 
from pos.views import CurrencyViewSet, SalesViewSet, SalesItemViewSet, SalesDailyUSDViewSet, SalesDailyZWLViewSet, SalesMonthlyUSDViewSet, \
    SalesMonthlyZWLViewSet, SalesItemDailyProductUSDViewSet, SalesItemDailyProductZWLViewSet, ProductSalesItemMonthlyUSDViewSet, \
    ProductSalesItemMonthlyZWLViewSet, UserMonthlySalesViewSet, UserDailySalesViewSet, SalesAllByUserViewSet, SalesLatestByUserViewSet, \
    CurrentUserSalesDailyViewset, CurrentUserSalesMonthlyViewset, \
    AllSalesItemByDayUSDViewSet, AllSalesItemByDayPaginatedUSDViewSet, AllSalesItemByDayZWLViewSet, AllSalesItemByDayPaginatedZWLViewSet



router = routers.DefaultRouter()
""" APP INFO """
router.register('app-info', AppInfoViewSet, basename='app-info-viewset')
# ----------------------
router.register('product', ProductViewSet, basename='product')
router.register('product-stock', ProductStockViewSet, basename='product-stock')
router.register('category', CategoryViewSet, basename='category')
router.register('currency', CurrencyViewSet, basename='currency')
router.register('users', UserAllViewSet, basename='users-all')
# -------------- PRICE --------------------
router.register('product-price', ProductPriceViewSet, basename='product-price')
# ---------------------- SALES ---------------------
router.register('sales', SalesViewSet, basename='sales')
router.register('sales/daily/usd', SalesDailyUSDViewSet, basename='sales-daily-usd')
router.register('sales/daily/zwl', SalesDailyZWLViewSet, basename='sales-daily-zwl')
router.register('sales/monthly/usd', SalesMonthlyUSDViewSet, basename='sales-monthly-usd')
router.register('sales/monthly/zwl', SalesMonthlyZWLViewSet, basename='sales-monthly-zwl')
router.register('salesitem', SalesItemViewSet, basename='salesitem')
router.register('salesitem/daily/product/usd', SalesItemDailyProductUSDViewSet, basename='salesitem-daily-product-usd')
router.register('sales/monthly/product/usd', ProductSalesItemMonthlyUSDViewSet, basename='sales-product-monthly-usd')
router.register('salesitem/daily/product/zwl', SalesItemDailyProductZWLViewSet, basename='salesitem-daily-product-zwl')
router.register('sales/monthly/product/zwl', ProductSalesItemMonthlyZWLViewSet, basename='sales-product-monthly-zwl')
router.register('sales/daily/byuser', UserDailySalesViewSet, basename='sales-daily-byuser')
router.register('sales/monthly/byuser', UserMonthlySalesViewSet, basename='sales-monthly-byuser')
router.register('sales/byuser/all', SalesAllByUserViewSet, basename='sales-byuser-all')
router.register('sales/byuser/latest', SalesLatestByUserViewSet, basename='sales-byuser-latest')
router.register('current-userdaily/sales', CurrentUserSalesDailyViewset, basename='sales-daily-current-user')
router.register('current-usermonthly/sales', CurrentUserSalesMonthlyViewset, basename='sales-monthly-current-user')
router.register('all-salesitem-byday/usd', AllSalesItemByDayUSDViewSet, basename='all-salesitem-byday-usd')
router.register('all-salesitem-byday-paginated/usd', AllSalesItemByDayPaginatedUSDViewSet, basename='all-salesitem-byday-paginated-usd')
router.register('all-salesitem-byday/zwl', AllSalesItemByDayZWLViewSet, basename='all-salesitem-byday-zwl')
router.register('all-salesitem-byday-paginated/zwl', AllSalesItemByDayPaginatedZWLViewSet, basename='all-salesitem-byday-paginated-zwl')
# ---------------------- SUPPLIER ----------------------
router.register('supplier', SupplierViewSet)
# ---------------------- PURCHASE ----------------------
router.register('purchase', PurchaseViewSet)
router.register('purchase-daily/usd', PurchaseDailyUSDViewSet, basename='purchase-daily-usd')
router.register('purchase-daily/zwl', PurchaseDailyZWLViewSet, basename='purchase-daily-zwl')
router.register('purchase-item', PurchaseItemViewSet)
router.register('purchase-item-daily/usd', PurchaseItemDailyProductUSDViewSet, basename='purchase-item-daily-usd')
router.register('purchase-item-daily/zwl', PurchaseItemDailyProductZWLViewSet, basename='purchase-item-daily-zwl')
router.register('purchase-item-monthly/usd', PurchaseItemMonthlyProductUSDViewSet, basename='purchase-item-monthly-usd')
router.register('purchase-item-monthly/zwl', PurchaseItemMonthlyProductZWLViewSet, basename='purchase-item-monthly-zwl')
router.register('purchase-item-byday/usd', AllPurchaseItemByDayUSDViewSet, basename='purchase-item-byday-usd')
router.register('purchase-item-byday/zwl', AllPurchaseItemByDayZWLViewSet, basename='purchase-item-byday-zwl')
router.register('purchase-item-byday-paginated/usd', AllPurchaseItemByDayPaginatedUSDViewSet, basename='purchase-item-byday-paginated-usd')
router.register('purchase-item-byday-paginated/zwl', AllPurchaseItemByDayPaginatedZWLViewSet, basename='purchase-item-byday-paginated-zwl')

router.register('purchase-supplier-monthly', PurchaseMonthlySupplierViewSet, basename='purchase-supplier-monthly')
router.register('purchase-supplier-daily', PurchaseDailySupplierViewSet, basename='purchase-supplier-daily')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]
