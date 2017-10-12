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
		response = Client().get('/add-friend/')
		self.assertEqual(response.status_code, 200)

	def test_add_friend_using_index_func(self):
		found = resolve('/lab-4/')
		self.assertEqual(found.func, index)

	def test_model_can_create_add_friend(self):
		#Creating a new activity
		new_activity = Add_Friend.objects.create(name='Tom Riddle',url='http://tom.herokuapp.com')

		#Retrieving all available activity
		counting_all_available_Friend= Add_Friend.objects.all().count()
		self.assertEqual(counting_all_available_Friend,1)

	def test_form_Friend_input_has_placeholder_and_css_classes(self):
		form = Add_Friend_Form()
		self.assertIn('class="form-control"', form.as_p())
		self.assertIn('<label for="id_name">Nama:</label>', form.as_p())
		self.assertIn('<label for="id_url">url:</label>', form.as_p())

	def test_form_validation_for_blank_items(self):
		form = Add_Friend_Form(data={'name': '', 'url': ''})
		self.assertFalse(form.is_valid())
		
			
	def test_addfriend_post_fail(self):
		response = Client().post('/add_friend/', {'name': 'Anonymous', 'url': 'A'})
		self.assertEqual(response.status_code, 302)

	def test_addfriend_post_success_and_render_the_result(self):
		anonymous = 'Anonymous'
		response = Client().post('/add_friend/', {'name': '', 'url': ''})
		self.assertEqual(response.status_code, 200)
		html_response = response.content.decode('utf8')
		self.assertIn(anonymous,html_response)
		

	'''
	def test_lab_4_table_using_Friend_table_func(self):
		found = resolve('/lab-4/result_table')
		self.assertEqual(found.func, friend_table)
	'''
		
	def test_lab_4_showing_all_Friends(self):
		name_budi = 'Budi'
		url_budi = 'http://budi.herokuapp.com'
		data_budi = {'name': name_budi, 'url': url_budi}
		post_data_budi = Client().post('/add_friend/', data_budi)
		self.assertEqual(post_data_budi.status_code, 200)

		Friend_anonymous = 'Masih Jelek Nih'
		data_anonymous = {'name': '', 'url': ''}
		post_data_anonymous = Client().post('/add_friend/', data_anonymous)
		self.assertEqual(post_data_anonymous.status_code, 200)

		response = Client().get('/add_friend/')
		html_response = response.content.decode('utf8')

		for key,data in data_budi.items():
			self.assertIn(data,html_response)

		self.assertIn('Anonymous', html_response)
		
		
	def test_root_url_now_is_using_index_page_from_lab_4(self):
		response = Client().get('/')
		self.assertEqual(response.status_code, 301)
		self.assertRedirects(response,'/add_friend/',301,200)
