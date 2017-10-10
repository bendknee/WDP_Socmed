from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index

class ProfilePageUnitTest(TestCase):
	def test_profile_page_url_is_exist(self):
		response = Client().get('')
		self.assertEqual(response.status_code, 200)

	def test_profilepage_using_index_func(self):
		found = resolve('/profile-page/')
		self.assertEqual(found.func, index)