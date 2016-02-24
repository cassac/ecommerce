from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class MailingAddress(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	address_line_1 = models.CharField(max_length=100)
	address_line_2 = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=50)
	state_province = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=20)
	country = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "<MailingAddress: %d - %s>" % (self.user.id, self.user.username)	