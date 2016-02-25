from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product, ProductVariation


class ProductVariationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProductVariation
		fields = ('product', 'category', 'title', 'image', 'price', 'active',
			'length', 'width', 'height', 'updated', 'url')

class ProductSerializer(serializers.HyperlinkedModelSerializer):

	productvariation_set = ProductVariationSerializer(many=True, read_only=True)

	class Meta:
		model = Product
		fields = ('id', 'slug', 'url', 'title', 'description', 'price', 
			'sale_price', 'active', 'productvariation_set')