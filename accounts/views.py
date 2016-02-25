from django.contrib.auth.models import User
from accounts.permissions import ViewIfAdminOrSelf, EditIfAdminOrSelf
from accounts.models import MailingAddress
from accounts.serializers import MailingAddressSerializer, UserSerializer
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.request import Request

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAdminUser,)

	@detail_route(methods=['GET', 'PUT'], permission_classes=[ViewIfAdminOrSelf])
	def mailingaddress(self, request, pk=None):
		print 'PK: ', pk
		serializer_context = {
		    'request': Request(request),
		}
		queryset = User.objects.get(pk=pk).mailingaddress_set.all()
		serializer = MailingAddressSerializer(queryset, many=True, read_only=True, context=serializer_context)
		return Response(serializer.data)

class MailingAddressViewSet(viewsets.ModelViewSet):

	queryset = MailingAddress.objects.all()
	serializer_class = MailingAddressSerializer
	permission_classes = (EditIfAdminOrSelf,)
