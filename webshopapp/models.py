from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    rebate_quantity = models.IntegerField()
    rebate_percent = models.DecimalField(max_digits=5, decimal_places=2)
    upsell_product_id = models.IntegerField()
    amount_in_stock = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.currency} {self.price}"

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=20, blank=True, null=True)
    order_comment = models.TextField(blank=True, null=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    vat = models.CharField(max_length=50, blank=True, null=True)
    delivery_country = models.CharField(max_length=100, blank=True, null=True)
    delivery_address1 = models.CharField(max_length=255, blank=True, null=True)
    delivery_address2 = models.CharField(max_length=255, blank=True, null=True)
    delivery_zip = models.CharField(max_length=12, blank=True, null=True)
    delivery_city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class BasketItem(models.Model):
    id = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalLinePrice = models.DecimalField(max_digits=10, decimal_places=2)
    rebatePercent = models.DecimalField(max_digits=5, decimal_places=2)
    giftwrapping = models.BooleanField()
    order = models.ForeignKey('Order', related_name='basket_items', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - Qty: {self.quantity}"

class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.order_number} for {self.customer}"
