from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'slug', 'url', 'title', 'description', 'price', 'sale_price', 'active')