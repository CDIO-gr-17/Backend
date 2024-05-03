from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='event-list'),
    path('create/', views.EventCreateView.as_view(), name='event-create'),
]