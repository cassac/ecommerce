from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from products import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
