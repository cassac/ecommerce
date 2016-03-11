from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings
# from .models import 

class UserTestCase(TestCase):
	def setUp(self):
		u = User.objects.create(
			first_name='Test',
			last_name='User',
			username='testuser',
			email='test@example.com',
			)
		u.save()
		u.set_password('testuser')

	def test_user_created(self):
		user = User.objects.first()
		self.assertEqual(user.username, 'testuser')