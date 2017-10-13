from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
response = {'author': "Hepzibah Sith"} #TODO Implement yourname
birthday = '13 Jan 1057'
gender =  'Male'
expertise = 'Marketing Collector Public Speaking'
description = 'Antique expert, Experience as marketer for 10 years'
email = 'hello@sith.com'

def index(request):
	html = 'profile_page/profile_page.html'
	response['birthday'] = birthday
	response['gender'] = gender
	response['expertise'] = expertise
	response['description'] = description
	response['email'] = email
	return render(request, html, response)
