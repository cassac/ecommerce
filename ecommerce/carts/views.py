from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from carts.models import Cart, CartItem
from products.models import ProductVariation
from carts.serializers import CartSerializer, CartItemSerializer


class CartListView(APIView):

	def get(self, request):

		if not request.session.get('cart_id'):
			cart = Cart.objects.create()
			request.session['cart_id'] = cart.id
		context={'request': request}
		cart = Cart.objects.get(pk=request.session.get('cart_id'))
		serializer = CartSerializer(cart, context=context)
		data = serializer.data

		details = {'details': 'cart retrieved',
				   'total_cart_items': len(cart.cartitems.all()),
				   }

		details.update(data) # combines returned serializer and details dictionary

		return Response(details)	


class CartItemView(APIView):

	def put(self, request, product_variation_id):

		quantity = int(request.query_params.get('quantity', 1))

		if not request.session.get('cart_id'):
			cart = Cart.objects.create()
			request.session['cart_id'] = cart.id

		cart = Cart.objects.get(pk=request.session.get('cart_id'))

		product_variation = ProductVariation.objects.get(pk=product_variation_id)

		found_match = False # If product already in cart then remove else add

		for cartitem in cart.cartitems.all():

			if len(cartitem.variation.all().filter(title=product_variation.title)) > 0\
				and cartitem.product.id == product_variation.product.id:

				found_match = True # Set to True so CartItem won't be created below

				if quantity != cartitem.quantity: # If difference in new quantity vs old quantity, user is updating not deleting
					cartitem.quantity = quantity
					cartitem.save()
				else:
					cartitem.delete() # Else user is deleting

		if not found_match:
			new_item = CartItem(
				cart=cart, 
				product=product_variation.product,
				quantity=quantity,
				)
			new_item.save()
			new_item.variation.add(product_variation)
		context={'request': request}
		serializer = CartSerializer(cart, context=context)
		data = serializer.data

		details = {'details': 'cart updated',
				   'total_cart_items': len(cart.cartitems.all()),
				   }

		details.update(data) # combines returned serializer and details dictionary

		return Response(details)