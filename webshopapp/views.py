from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Event, Customer, basketItems, Order
from .serializers import EventSerializer
from django.db import transaction

@api_view(['GET'])
class EventCreateView(generics.CreateAPIView):
    # queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            # Extracting Customer data
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
                telephone_number=customer_data['telephone_number'],
                order_comment=customer_data.get('order_comment', ''),
                vat=customer_data.get('vat', ''),
                business_name=customer_data.get('business_name', ''),
                delivery_address1=customer_data.get('delivery_address1', ''),
                delivery_address2=customer_data.get('delivery_address2', ''),
                delivery_city=customer_data.get('delivery_city', ''),
                delivery_country=customer_data.get('delivery_country', ''),
                delivery_zip=customer_data.get('delivery_zip', '')
            )

            # Extracting and creating BasketItem data
            basket_items_data = request.data['basketItems']
            for item in basket_items_data:
                BasketItem.objects.create(
                    product_id=item['productId'],
                    quantity=item['quantity'],
                    rebate_percent=item['rebatePercent'],
                    total_line_price=item['totalLinePrice'],
                    giftwrapping=item['giftwrapping'],
                )

            order = Order.objects.create(
                customer=customer,
                basketLine=basket_item
            )
            orders.append(order)

            # Optionally, create or update an Event instance if needed
            # Event-specific data handling here
            # event_instance = handle_event_creation_or_updating()

        return Response({"status": "success"})

# class EventCreateView(generics.CreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     http_method_names = ['post']

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get']