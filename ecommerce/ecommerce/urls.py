from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from rest_framework.routers import DefaultRouter

from accounts import views as AccountsViews
from products import views as ProductsViews
from carts import views as CartsViews

router = DefaultRouter()
router.register(r'users', AccountsViews.UserViewSet)
router.register(r'mailingaddress', AccountsViews.MailingAddressViewSet)
router.register(r'products', ProductsViews.ProductViewSet)
router.register(r'productvariation', ProductsViews.ProductVariationViewSet)
router.register(r'productimage', ProductsViews.ProductImageViewSet)

urlpatterns = [
	url(r'^login/$', AccountsViews.login_view, name='user-login'),
	url(r'^accounts/', include('accounts.urls')),
	url(r'^products/', include('products.urls')),
	url(r'^carts/', include('carts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}), 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': settings.DEBUG}),       
]
