from django.conf.urls import url
from .views import index, update_status

urlpatterns=[
    url(r'^$', index, name='index'),
    url(r'^update_status/', update_status,name='update_status'),
]
