from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Customer, BasketItem, Order
from .serializers import EventSerializer
from django.db import transaction

from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db import transaction
from .models import Customer, BasketItem, Order
from .serializers import EventSerializer

class EventCreateView(generics.CreateAPIView):
    serializer_class = EventSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            customer_data = request.data['customerInfo']
            customer = Customer.objects.create(
                first_name=customer_data['first_name'],
                last_name=customer_data['last_name'],
                email=customer_data['email'],
                address1=customer_data['address1'],
                address2=customer_data.get('address2', ''),
                city=customer_data['city'],
                zip_code=customer_data['zip_code'],
                country=customer_data['country'],
                telephone_number=customer_data.get('telephone_number', ''),
                order_comment=customer_data.get('order_comment', ''),
                vat=customer_data.get('vat', ''),
                business_name=customer_data.get('business_name', ''),
                delivery_address1=customer_data.get('delivery_address1', ''),
                delivery_address2=customer_data.get('delivery_address2', ''),
                delivery_city=customer_data.get('delivery_city', ''),
                delivery_country=customer_data.get('delivery_country', ''),
                delivery_zip=customer_data.get('delivery_zip', '')
            )

            orders = []
            basket_items_data = request.data['basketItems']
            for item in basket_items_data:
                basket_item = BasketItem.objects.create(
                    product_id=item['productId'],
                    quantity=item['quantity'],
                    rebate_percent=item['rebatePercent'],
                    total_line_price=item['totalLinePrice'],
                    giftwrapping=item['giftwrapping']
                )
                order = Order.objects.create(
                    customer=customer,
                    basketLine=basket_item
                )
                orders.append(order)

            return Response({"status": "success", "orders": [order.orderNumber for order in orders]})

class EventListView(generics.ListAPIView):
    #queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get']