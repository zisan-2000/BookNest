from django.contrib import admin
from .models import (
    Country, Address, SiteUser, UserAddress, PaymentType, UserPaymentMethod,
    ProductCategory, Product, Variation, VariationOption, ProductItem, ProductConfiguration,
    ShoppingCart, ShoppingCartItem, ShippingMethod, OrderStatus, ShopOrder, OrderLine,
    Promotion, PromotionCategory, UserReview
)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name')
    search_fields = ('country_name',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address_line1', 'city', 'postal_code', 'country')
    search_fields = ('address_line1', 'city', 'postal_code')
    list_filter = ('city', 'country')


@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email_address', 'phone_number')
    search_fields = ('email_address', 'phone_number')


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'is_default')
    search_fields = ('user__email_address', 'address__address_line1')


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    search_fields = ('value',)


@admin.register(UserPaymentMethod)
class UserPaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_type', 'provider', 'account_number', 'expiry_date', 'is_default')
    search_fields = ('user__email_address', 'provider')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'parent_category')
    search_fields = ('category_name',)
    list_filter = ('parent_category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
    search_fields = ('name', 'category__category_name')
    list_filter = ('category',)


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name', 'category__category_name')
    list_filter = ('category',)


@admin.register(VariationOption)
class VariationOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'variation', 'value')
    search_fields = ('variation__name', 'value')


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'SKU', 'qty_in_stock', 'price')
    search_fields = ('SKU', 'product__name')
    list_filter = ('product',)


@admin.register(ProductConfiguration)
class ProductConfigurationAdmin(admin.ModelAdmin):
    list_display = ('product_item', 'variation_option')
    search_fields = ('product_item__SKU', 'variation_option__value')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__email_address',)


@admin.register(ShoppingCartItem)
class ShoppingCartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product_item', 'qty')
    search_fields = ('cart__user__email_address', 'product_item__SKU')


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    search_fields = ('status',)


@admin.register(ShopOrder)
class ShopOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'order_total', 'order_status')
    search_fields = ('user__email_address',)
    list_filter = ('order_status', 'order_date')


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product_item', 'qty', 'price')
    search_fields = ('order__user__email_address', 'product_item__SKU')


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discount_rate', 'start_date', 'end_date')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')


@admin.register(PromotionCategory)
class PromotionCategoryAdmin(admin.ModelAdmin):
    list_display = ('promotion', 'category')
    search_fields = ('promotion__name', 'category__category_name')


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'ordered_product', 'rating_value')
    search_fields = ('user__email_address', 'ordered_product__SKU')
    list_filter = ('rating_value',)
