from django.contrib.auth.models import User
from accounts.permissions import IsOwnerOrReadOnly, EditUserIsAdminOrUser
from accounts.models import MailingAddress
from accounts.serializers import MailingAddressSerializer, UserSerializer
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
	                     EditUserIsAdminOrUser)

	@detail_route(methods=['GET', 'PUT'], permission_classes=[], url_path='mailingaddress')
	def mailingaddress(self, request, pk):
		queryset = User.objects.get(pk=pk).mailingaddress_set.all()
		serializer = MailingAddressSerializer(queryset, many=True, read_only=True)
		return Response(serializer.data)

class MailingAddressViewSet(viewsets.ModelViewSet):

	queryset = MailingAddress.objects.all()
	serializer_class = MailingAddressSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
	                      IsOwnerOrReadOnly,)
	def perform_create(self, instance):
		serializer = MailingAddressSerializer(instance, partial=True)
		serializer.save(owner=self.request.user)
