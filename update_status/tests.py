from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
# Create your tests here.

class UpdateStatusUnitTest(TestCase):

    def test_status_url_is_exist(self):
        response = Client().get('/status/')
        self.assertEqual(response.status_code, 200)

    def test_status_is_using_index_func(self):
        found = resolve('/status/')
        self.assertEqual(found.func, index)

    def root_is_using_status_url(self):
        response = Client().get('/')
        self.assertEqual(response.status_code,301)
        self.assertRedirect(response,'/status/',301,200)
