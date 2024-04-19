from django.db import models

#      Create your models here.
# class Event(models.Model):
#     about = models.TextField()
#     event_id = models.CharField(max_length=255)
#     workflow_id = models.CharField(max_length=255)
#     owner_id = models.CharField(max_length=255)
#     deployment_id = models.CharField(max_length=255)
#     timestamp = models.DateTimeField()
#     inspect_url = models.URLField()
#     quickstart_url = models.URLField()




#     def __str__(self):
#         return self.about
    
class Event(models.Model):
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