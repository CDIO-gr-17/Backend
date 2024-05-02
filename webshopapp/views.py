from rest_framework.response import Response
from rest_framework import generics
from .models import Order
from .serializers import CustomerSerializer, BasketItemSerializer
from django.db import transaction
from rest_framework import status

class EventCreateView(generics.CreateAPIView):
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):

        with transaction.atomic():
            customer_serializer = CustomerSerializer(data=request.data['customerInfo'])
            customer_serializer.is_valid(raise_exception=True)
            customer = customer_serializer.save()

            order = Order.objects.create(customer=customer)

            basket_items_data = request.data.get('basketItems', [])
            for item in basket_items_data:

                item['order'] = order.order_number

                print(item)

                basket_item_serializer = BasketItemSerializer(data=item)
                basket_item_serializer.is_valid(raise_exception=True)
                basket_item_serializer.save()

            return Response({
                "status": "success",
                "order_number": order.order_number,
                "customer": f"{customer.first_name} {customer.last_name}",
                "num_items": len(basket_items_data)
            })

class EventListView(generics.ListAPIView):
    #queryset = Event.objects.all()
    # serializer_class = EventSerializer
    http_method_names = ['get']