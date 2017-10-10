from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, update_status
# Create your tests here.

class UpdateStatusUnitTest(TestCase):

    def test_status_url_is_exist(self):
        response = Client().get('/status/')
        self.assertEqual(response.status_code, 200)

    def test_status_is_using_index_func(self):
        found = resolve('/status/')
        self.assertEqual(found.func, index)

    def test_root_is_using_status_url(self):
        response = Client().get('/')
        self.assertEqual(response.status_code,301)
        self.assertRedirects(response,'/status/',301,200)

    def test_post_status_url_is_exist(self):
        status = 'I pwn U'
        response_post = Client().post('/status/update_status/', {'status': status})
        self.assertEqual(response_post.status_code, 302)

    def test_post_status_url_is_using_update_status_func(self):
        found = resolve('/status/update_status/')
        self.assertEqual(found.func, update_status)
