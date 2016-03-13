from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^item/(?P<product_variation_id>[0-9]*)$', views.CartItemView.as_view(), name='cart-item'),
]