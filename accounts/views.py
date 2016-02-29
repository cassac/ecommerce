from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from accounts.permissions import ViewIfAdminOrSelf, EditIfAdminOrSelf
from accounts.models import MailingAddress
from accounts.serializers import MailingAddressSerializer, UserSerializer
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.request import Request
import json
from django.contrib.auth import authenticate, login, logout

def login_view(request):
	print 'login request'
	if request.method == 'POST':
		data = json.loads(request.body)
		username = data['username']
		password = data['password']
		print data['username']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return JsonResponse({'detail': 'successful login'})		
		# username = request.POST['username']
		# password = request.POST['password']

		# print username
		# print password
	return JsonResponse({'detail': 'failed login'})


def user_mailing_address(request):
	context = {'foo': 'variable from view'}
	return render(request, 'accounts/mailingaddress.html', context)

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
