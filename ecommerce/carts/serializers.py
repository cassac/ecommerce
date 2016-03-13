from django.contrib.auth.models import User
from rest_framework import serializers
from carts.models import Cart, CartItem


class CartSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cart
		fields = ('__all__')

class CartItemSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CartItem
		fields = ('__all__')