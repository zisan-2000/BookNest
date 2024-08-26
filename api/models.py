from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class Address(models.Model):
    unit_number = models.CharField(max_length=10, blank=True, null=True)
    street_number = models.CharField(max_length=20, blank=True, null=True)
    address_line1 = models.CharField(max_length=191)
    address_line2 = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='addresses')

    def __str__(self):
        return f"{self.address_line1}, {self.city}, {self.country}"


class SiteUser(models.Model):
    email_address = models.EmailField(max_length=191, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email_address


class UserAddress(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='addresses')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"Address for {self.user.email_address}"


class PaymentType(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class UserPaymentMethod(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='payment_methods')
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    expiry_date = models.DateField()
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.provider} for {self.user.email_address}"


class ProductCategory(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Variation(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='variations')
    name = models.CharField(max_length=191)

    def __str__(self):
        return self.name


class VariationOption(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, related_name='options')
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')
    SKU = models.CharField(max_length=50, unique=True)
    qty_in_stock = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.SKU}"


class ProductConfiguration(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='configurations')
    variation_option = models.ForeignKey(VariationOption, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('product_item', 'variation_option'),)

    def __str__(self):
        return f"Configuration for {self.product_item.SKU}"


class ShoppingCart(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='shopping_carts')

    def __str__(self):
        return f"Cart for {self.user.email_address}"


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='items')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.qty} x {self.product_item.SKU} in {self.cart}"


class ShippingMethod(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class ShopOrder(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.ForeignKey(UserPaymentMethod, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id} by {self.user.email_address}"


class OrderLine(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    order = models.ForeignKey(ShopOrder, on_delete=models.CASCADE, related_name='order_lines')
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.qty} x {self.product_item.SKU} in order #{self.order.id}"


class Promotion(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class PromotionCategory(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('category', 'promotion'),)

    def __str__(self):
        return f"{self.promotion.name} for {self.category.category_name}"


class UserReview(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    ordered_product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    rating_value = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Review by {self.user.email_address} for {self.ordered_product.SKU}"
