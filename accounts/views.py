from accounts.models import MailingAddress
from accounts.serializers import MailingAddressSerializer, UserSerializer
from rest_framework import generics

from django.contrib.auth.models import User

# ViewSets define the view behavior.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MailingAddressList(generics.ListCreateAPIView):
    queryset = MailingAddress.objects.all()
    serializer_class = MailingAddressSerializer

class MailingAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MailingAddress.objects.all()
    serializer_class = MailingAddressSerializer