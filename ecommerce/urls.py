from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from accounts import views as AccountsViews
from products import views as ProductsViews

router = DefaultRouter()
router.register(r'users', AccountsViews.UserViewSet)
router.register(r'mailingaddress', AccountsViews.MailingAddressViewSet)
router.register(r'products', ProductsViews.ProductViewSet)
router.register(r'productvariation', ProductsViews.ProductVariationViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))   
]
