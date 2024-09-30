from rest_framework import viewsets
from .models import (
    Country, Address, SiteUser, UserAddress, PaymentType, UserPaymentMethod,
    ProductCategory, Product, Variation, VariationOption, ProductItem, ProductConfiguration,
    ShoppingCart, ShoppingCartItem, ShippingMethod, OrderStatus, ShopOrder, OrderLine,
    Promotion, PromotionCategory, UserReview, Vendor, Inventory, Writer, Publisher
)

from .serializers import (
    CountrySerializer, AddressSerializer, SiteUserSerializer, UserAddressSerializer,
    PaymentTypeSerializer, UserPaymentMethodSerializer, ProductCategorySerializer, ProductSerializer,
    VariationSerializer, VariationOptionSerializer, ProductItemSerializer, ProductConfigurationSerializer,
    ShoppingCartSerializer, ShoppingCartItemSerializer, ShippingMethodSerializer, OrderStatusSerializer,
    ShopOrderSerializer, OrderLineSerializer, PromotionSerializer, PromotionCategorySerializer,
    UserReviewSerializer, VendorSerializer, InventorySerializer, WriterSerializer, PublisherSerializer
)

# Create a viewset for each model

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class SiteUserViewSet(viewsets.ModelViewSet):
    queryset = SiteUser.objects.all()
    serializer_class = SiteUserSerializer


class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class UserPaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = UserPaymentMethod.objects.all()
    serializer_class = UserPaymentMethodSerializer


# Viewset for Writer
class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

# Viewset for Publisher
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer


class VariationOptionViewSet(viewsets.ModelViewSet):
    queryset = VariationOption.objects.all()
    serializer_class = VariationOptionSerializer


class ProductItemViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


class ProductConfigurationViewSet(viewsets.ModelViewSet):
    queryset = ProductConfiguration.objects.all()
    serializer_class = ProductConfigurationSerializer


# Viewset for Vendor
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

# Viewset for Inventory
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class ShoppingCartItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer


class ShippingMethodViewSet(viewsets.ModelViewSet):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class ShopOrderViewSet(viewsets.ModelViewSet):
    queryset = ShopOrder.objects.all()
    serializer_class = ShopOrderSerializer


class OrderLineViewSet(viewsets.ModelViewSet):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionCategoryViewSet(viewsets.ModelViewSet):
    queryset = PromotionCategory.objects.all()
    serializer_class = PromotionCategorySerializer


class UserReviewViewSet(viewsets.ModelViewSet):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer


