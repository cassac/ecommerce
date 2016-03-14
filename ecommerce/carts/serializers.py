from django.contrib.auth.models import User
from rest_framework import serializers
from carts.models import Cart, CartItem
from products.models import ProductVariation


class VariationSerializer(serializers.HyperlinkedModelSerializer):

	image = serializers.ImageField(source='get_image')

	class Meta:
		model = ProductVariation
		fields = ('id', 'title', 'image')

class CartItemSerializer(serializers.ModelSerializer):

	variation = VariationSerializer(many=True)

	class Meta:
		model = CartItem
		fields = ('id', 'product', 'variation')#, 'image')

class CartSerializer(serializers.ModelSerializer):

	cartitems = CartItemSerializer(many=True)

	class Meta:
		model = Cart
		fields = ('id', 'cartitems')
