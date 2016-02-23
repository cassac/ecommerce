from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^ma/$', views.MailingAddressList.as_view()),
    url(r'^ma/(?P<pk>[0-9]+)/$', views.MailingAddressDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)