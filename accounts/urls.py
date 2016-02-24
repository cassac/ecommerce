from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from accounts import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'mailingaddress', views.MailingAddressViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
