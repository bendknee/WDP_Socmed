from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
from add_friend.models import Add_Friend
from update_status.models import Status

class StatisticPageUnitTest(TestCase):
    def test_statistic_page_url_is_exist(self):
        response = Client().get('/statistic/')
        self.assertEqual(response.status_code, 200)

    def test_statistic_page_using_index_func(self):
        found = resolve('/statistic/')
        self.assertEqual(found.func, index)

    def test_status_counter_is_working(self):
        Status.objects.create(status = 'I play dota everyday~')
        Status.objects.create(status = 'Tupperware is dead')
        count = Status.objects.count()
        response = Client().get('/statistic/')
        html_response = response.content.decode('utf8')
        self.assertIn(str(count), html_response)

    def test_friend_counter_is_working(self):
        Add_Friend.objects.create(name='Tom Riddle', url='http://tom.herokuapp.com')
        Add_Friend.objects.create(name='Tom Edison', url='http://tesla.herokuapp.com')
        count = Add_Friend.objects.count()
        response = Client().get('/statistic/')
        html_response = response.content.decode('utf8')
        self.assertIn(str(count), html_response)

    def test_last_post_is_shown(self):
        Status.objects.create(status = 'I play dota everyday~')
        Status.objects.create(status = 'Tupperware is dead')
        response = Client().get('/statistic/')
        html_response = response.content.decode('utf8')
        self.assertIn('Tupperware is dead', html_response)
