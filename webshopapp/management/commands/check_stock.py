from django.core.management.base import BaseCommand
from webshopapp.models import Product
import requests  # Import for making HTTP requests

class Command(BaseCommand):
  help = 'Check stock levels and send Discord notifications'

  def handle(self, *args, **options):
    # Define the Discord webhook URL (replace with your actual URL)
    webhook_url = "https://discord.com/api/webhooks/1235581621386608691/n7k-3-Q_3nACH6U98pP4BIxwszbGKyYNSpgt2GfhkfphFPvPigUxmIW7drzXKlfxB5Fd"

    low_stock_products = Product.objects.filter(amount_in_stock__lt=5)
    super_low_stock_products = Product.objects.filter(amount_in_stock__lt=0)

    if low_stock_products:  # Check if any products have low stock
      message = "**Low Stock Products:**\n"
      for product in low_stock_products:
          message += f"- Product ID: {product.id}, Product Name: {product.name}, Amount in Stock: {product.amount_in_stock}\n"


      payload = {"content": message}
      response = requests.post(webhook_url, json=payload)
      response.raise_for_status()  # Raise exception for non-2xx response codes
      print("Successfully sent notification for low-stock products.")
    else:
      print("No products with low stock found.")

    if super_low_stock_products:  # Check if any products have super low stock
      for product in super_low_stock_products:
        product.amount_in_stock = 10  # Reset the stock level to 10
        product.save()

if __name__ == "__main__":
  # Execute the command
  command = Command()
  command.handle()
