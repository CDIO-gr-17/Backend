from django.core.management.base import BaseCommand
from webshopapp.models import Product

class Command(BaseCommand):
    help = 'Check stock levels'

    def handle(self, *args, **options):
        low_stock_products = Product.objects.filter(amount_in_stock__lt=5)
        for product in low_stock_products:
            print(f'Product ID: {product.id}, Product Name: {product.name}, Amount in Stock: {product.amount_in_stock}')