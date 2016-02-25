from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from products.permissions import EditIfIsAdminUser
from products.models import Product, ProductVariation, ProductImage
from products.serializers import (ProductSerializer, ProductVariationSerializer, 
	ProductImageSerialzer)

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = (EditIfIsAdminUser,)

	@detail_route(methods=['GET', 'PUT'], permission_classes=[], url_path='productvariation')
	def productvariation(self, request, pk):
		queryset = Product.objects.get(pk=pk).productvariation_set.all()
		serializer = ProductVariationSerializer(queryset, many=True, read_only=True)
		return Response(serializer.data)

class ProductVariationViewSet(viewsets.ModelViewSet):

	queryset = ProductVariation.objects.all()
	serializer_class = ProductVariationSerializer

class ProductImageViewSet(viewsets.ModelViewSet):

	queryset = ProductImage.objects.all()
	serializer_class = ProductImageSerialzer
