from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
response = {'author': "Hepzibah Smith"} #TODO Implement yourname
birthday = '01 jan'
gender =  'Female'
expertise = 'Marketing Collector Public Speaking'
description = 'Antique expert, Experience as marketer for 10 years'
email = 'hello@smith.com'

def index(request):
	html = 'profile_page/profile_page.html'
	response['birthday'] = birthday
	response['gender'] = gender
	response['expertise'] = expertise
	response['description'] = description
	response['email'] = email
	return render(request, html, response)
