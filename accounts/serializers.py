from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import MailingAddress


class MailingAddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MailingAddress
		fields = ('id', 'url', 'user', 'first_name', 'last_name', 'address_line_1',
			'address_line_2', 'city', 'state_province', 'postal_code',
			'country', 'phone')

class UserSerializer(serializers.HyperlinkedModelSerializer):

	mailingaddress_set = MailingAddressSerializer(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'email', 'is_staff', 
			'mailingaddress_set')