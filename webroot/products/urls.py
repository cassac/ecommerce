from django.conf.urls import url

from products import views

urlpatterns = [
    url(r'^$', views.display_products, name='products'),           
]