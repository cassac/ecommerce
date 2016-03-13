from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from carts.models import Cart, CartItem
from products.models import ProductVariation
from carts.serializers import CartSerializer, CartItemSerializer

class CartItemView(APIView):

	# SWITCH REQUEST METHOD
	def get(self, request, product_variation_id):

		if not request.session.get('cart_id'):
			cart = Cart.objects.create()
			request.session['cart_id'] = cart.id

		cart = Cart.objects.get(pk=request.session.get('cart_id'))

		product_variation = ProductVariation.objects.get(pk=product_variation_id)

		found_match = False # If product already in cart then remove else add
		for cartitem in cart.cartitem_set.all():
			if len(cartitem.variation.all().filter(title=product_variation.title))>0\
				and cartitem.product.id == product_variation.product.id:
				cartitem.delete() # If found then delete
				found_match = True # Set to True so CartItem won't be created below
				temp = {'details': 'item removed from cart'}

		if not found_match:
			new_item = CartItem(
				cart=cart, 
				product=product_variation.product,
				quantity=1,
				)
			new_item.save()
			new_item.variation.add(product_variation)
			temp = {'details': 'item added to cart'}

		print cart.cartitem_set.all()

		return Response(temp)