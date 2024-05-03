from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db import transaction
from .models import Customer, BasketItem, Order, BasketItem, Product
from .serializers import BasketItemSerializer, ProductSerializer, CustomerSerializer

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

                # Retrieve the product and update its warehouse quantity
                product = Product.objects.get(id=item.product.id)
                product.amount_in_stock -= basket_item_serializer.quantity
                product.save()

            return Response({
                "status": "success",
                "order_number": order.order_number,
                "customer": f"{customer.first_name} {customer.last_name}",
                "num_items": len(basket_items_data)
            })

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']
