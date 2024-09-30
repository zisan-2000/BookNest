from rest_framework import serializers
from .models import (
    Country, Address, SiteUser, UserAddress, PaymentType, UserPaymentMethod,
    ProductCategory, Product, Variation, VariationOption, ProductItem, ProductConfiguration,
    ShoppingCart, ShoppingCartItem, ShippingMethod, OrderStatus, ShopOrder, OrderLine,
    Promotion, PromotionCategory, UserReview, Vendor, Inventory, Writer, Publisher
)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Address
        fields = '__all__'

class SiteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUser
        fields = '__all__'


class UserAddressSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = UserAddress
        fields = '__all__'


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'


class UserPaymentMethodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserPaymentMethod
        fields = '__all__'


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

class VariationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Variation
        fields = '__all__'

class VariationOptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VariationOption
        fields = '__all__'

class ProductItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductItem
        fields = '__all__'

class ProductConfigurationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductConfiguration
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShoppingCart
        fields = '__all__'

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShoppingCartItem
        fields = '__all__'

class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = '__all__'

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class ShopOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShopOrder
        fields = '__all__'

class OrderLineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderLine
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

class PromotionCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PromotionCategory
        fields = '__all__'

class UserReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserReview
        fields = '__all__'


