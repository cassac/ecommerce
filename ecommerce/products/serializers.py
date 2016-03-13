from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product, ProductVariation, ProductImage


class ProductVariationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProductVariation
		fields = ('id', 'product', 'category', 'title', 'image', 'price', 'active',
			'length', 'width', 'height', 'updated')

class ProductImageSerialzer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = ProductImage
		fields = ('url', 'product', 'image', 'active', 'updated')

class ProductSerializer(serializers.HyperlinkedModelSerializer):

	productvariation_set = ProductVariationSerializer(many=True, read_only=True)
	productimage_set = ProductImageSerialzer(many=True, read_only=True)

	class Meta:
		model = Product
		fields = ('id', 'slug', 'url', 'title', 'description', 'price', 
			'sale_price', 'active', 'productvariation_set', 'productimage_set')