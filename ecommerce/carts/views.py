from django.contrib.auth.models import User
from django.shortcuts import render
# DJANGO REST
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from carts.models import Cart, CartItem
from carts.serializers import CartSerializer, CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
	queryset = Cart.objects.all()
	serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
	queryset = CartItem.objects.all()
	serializer_class = CartItemSerializer