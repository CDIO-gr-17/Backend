from django.db import models


class Order(models.Model):
    orderNumber = models.AutoField(primary_key=True)
    customerNo = models.ForeignKey('Event', on_delete=models.CASCADE)
    basketLineId = models.ForeignKey('basketItems', on_delete=models.CASCADE)
    

class basketItems(models.Model):
    basketItemId = models.AutoField(primary_key=True)
    productId = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalLineprice = models.DecimalField(max_digits=10, decimal_places=2)
    rebatePercent = models.DecimalField(max_digits=5, decimal_places=2)
    giftWrapping = models.BooleanField()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    rebateQuantity = models.IntegerField()
    rebatePercent = models.DecimalField(max_digits=5, decimal_places=2)
    upsellProductId = models.IntegerField()
    amountInStock = models.IntegerField()
    
class Customer(models.Model):
    customerNo = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=20)
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