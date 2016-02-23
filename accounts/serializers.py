from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import MailingAddress


class MailingAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = MailingAddress
		fields = ('user', 'first_name', 'last_name', 'address_line_1',
			'address_line_2', 'city', 'state_province', 'postal_code',
			'country', 'phone')

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):

	mailingaddress_set = MailingAddressSerializer(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'email', 'is_staff', 
			'mailingaddress_set')