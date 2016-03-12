from django.conf.urls import url

from products import views

urlpatterns = [
    url(r'^shop$', views.display_products, name='products'),           
]