from unittest import skip

from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import index, add_friend
from .models import Add_Friend
from .forms import Add_Friend_Form


# Create your tests here.

class AddFriendUnitTest(TestCase):
    def test_add_friend_url_is_exist(self):
        response = Client().get('/friend/')
        self.assertEqual(response.status_code, 200)

    def test_add_friend_using_index_func(self):
        found = resolve('/friend/')
        self.assertEqual(found.func, index)

    def test_post_add_friend_using_add_friend_func(self):
        found = resolve('/friend/add_friend')
        self.assertEqual(found.func, add_friend)

    def test_model_can_create_add_friend(self):
        # Creating a new activity
        new_activity = Add_Friend.objects.create(name='Tom Riddle', url='http://tom.herokuapp.com')

        # Retrieving all available activity
        counting_all_available_Friend = Add_Friend.objects.all().count()
        self.assertEqual(counting_all_available_Friend, 1)

    '''
    @skip
    def test_form_Friend_input_has_placeholder_and_css_classes(self):
        form = Add_Friend_Form()
        self.assertIn('class="friend-name"', form.as_p())
        self.assertIn('<label for="id_name">Nama:</label>', form.as_p())
        self.assertIn('<label for="id_url">url:</label>', form.as_p())
    '''
    def test_form_validation_for_blank_items(self):
        form = Add_Friend_Form(data={'name': '', 'url': ''})
        self.assertFalse(form.is_valid())

    def test_addfriend_post_fail(self):
        response = Client().post('/friend/', {'name': '', 'url': ''})
        self.assertEqual(response.status_code, 200)

    '''
    @skip
    def test_addfriend_post_success_and_render_the_result(self):
        anonymous = 'Anonymous'
        response = Client().post('/friend/', {'name': 'Anonymous', 'url': 'Anonymous.herokuapp.com'})
        self.assertEqual(response.status_code, 200)
        html_response = response.content.decode('utf8')
        self.assertIn(anonymous, html_response)
    '''
    '''
    @skip
    def test_showing_all_Friends(self):
        name_budi = 'Budi'
        url_budi = 'http://budi.herokuapp.com'
        data_budi = {'name': name_budi, 'url': url_budi}
        post_data_budi = Client().post('/friend/', data_budi)
        self.assertEqual(post_data_budi.status_code, 200)

        response = Client().get('/friend/')
        html_response = response.content.decode('utf8')

        for key, data in data_budi.items():
            self.assertIn(data, html_response)
    '''
