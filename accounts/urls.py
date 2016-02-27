from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^mailing/$', views.user_mailing_address, name='mailing'),           
]