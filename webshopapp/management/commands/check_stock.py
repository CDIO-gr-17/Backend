from django.core.management.base import BaseCommand
from webshopapp.models import Product
import requests  # Import for making HTTP requests

class Command(BaseCommand):
  help = 'Check stock levels and send Discord notifications'

  def handle(self, *args, **options):
    low_stock_products = Product.objects.filter(amount_in_stock__lt=5)
    webhook_url = "https://discord.com/api/webhooks/1235581621386608691/n7k-3-Q_3nACH6U98pP4BIxwszbGKyYNSpgt2GfhkfphFPvPigUxmIW7drzXKlfxB5Fd"  # Replace with your actual webhook URL

    for product in low_stock_products:
      message = f"Product ID: {product.id}, Product Name: {product.name}, Amount in Stock: {product.amount_in_stock}"
      payload = {"content": message}  # Payload for Discord notification

      try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # Raise exception for non-2xx response codes
        print(f"Successfully sent Discord notification for product ID: {product.id}")
      except requests.exceptions.RequestException as e:
        print(f"Error sending Discord notification: {e}")

if __name__ == "__main__":
  # Execute the command
  command = Command()
  command.handle()
