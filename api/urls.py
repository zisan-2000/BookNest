from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CountryViewSet, AddressViewSet, SiteUserViewSet, UserAddressViewSet,
    PaymentTypeViewSet, UserPaymentMethodViewSet, ProductCategoryViewSet,
    ProductViewSet, VariationViewSet, VariationOptionViewSet, ProductItemViewSet,
    ProductConfigurationViewSet, ShoppingCartViewSet, ShoppingCartItemViewSet,
    ShippingMethodViewSet, OrderStatusViewSet, ShopOrderViewSet, OrderLineViewSet,
    PromotionViewSet, PromotionCategoryViewSet, UserReviewViewSet, VendorViewSet, InventoryViewSet, WriterViewSet, PublisherViewSet
)

router = DefaultRouter()

# Core Entities
router.register(r'countries', CountryViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'site-users', SiteUserViewSet)
router.register(r'user-addresses', UserAddressViewSet)
router.register(r'payment-types', PaymentTypeViewSet)
router.register(r'user-payment-methods', UserPaymentMethodViewSet)

# Product-related Models
router.register(r'writers', WriterViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'variations', VariationViewSet)
router.register(r'variation-options', VariationOptionViewSet)
router.register(r'product-items', ProductItemViewSet)
router.register(r'product-configurations', ProductConfigurationViewSet)

# Vendor and Inventory
router.register(r'vendors', VendorViewSet)
router.register(r'inventories', InventoryViewSet)

# Shopping and Orders
router.register(r'shopping-carts', ShoppingCartViewSet)
router.register(r'shopping-cart-items', ShoppingCartItemViewSet)
router.register(r'shipping-methods', ShippingMethodViewSet)
router.register(r'order-statuses', OrderStatusViewSet)
router.register(r'shop-orders', ShopOrderViewSet)
router.register(r'order-lines', OrderLineViewSet)

# Promotion and Reviews
router.register(r'promotions', PromotionViewSet)
router.register(r'promotion-categories', PromotionCategoryViewSet)
router.register(r'user-reviews', UserReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
