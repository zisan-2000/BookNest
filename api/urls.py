from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CountryViewSet, AddressViewSet, SiteUserViewSet, UserAddressViewSet,
    PaymentTypeViewSet, UserPaymentMethodViewSet, ProductCategoryViewSet,
    ProductViewSet, VariationViewSet, VariationOptionViewSet, ProductItemViewSet,
    ProductConfigurationViewSet, ShoppingCartViewSet, ShoppingCartItemViewSet,
    ShippingMethodViewSet, OrderStatusViewSet, ShopOrderViewSet, OrderLineViewSet,
    PromotionViewSet, PromotionCategoryViewSet, UserReviewViewSet
)

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'site-users', SiteUserViewSet)
router.register(r'user-addresses', UserAddressViewSet)
router.register(r'payment-types', PaymentTypeViewSet)
router.register(r'user-payment-methods', UserPaymentMethodViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'variations', VariationViewSet)
router.register(r'variation-options', VariationOptionViewSet)
router.register(r'product-items', ProductItemViewSet)
router.register(r'product-configurations', ProductConfigurationViewSet)
router.register(r'shopping-carts', ShoppingCartViewSet)
router.register(r'shopping-cart-items', ShoppingCartItemViewSet)
router.register(r'shipping-methods', ShippingMethodViewSet)
router.register(r'order-statuses', OrderStatusViewSet)
router.register(r'shop-orders', ShopOrderViewSet)
router.register(r'order-lines', OrderLineViewSet)
router.register(r'promotions', PromotionViewSet)
router.register(r'promotion-categories', PromotionCategoryViewSet)
router.register(r'user-reviews', UserReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
