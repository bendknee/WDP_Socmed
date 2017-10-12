from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Add_Friend_Form
from .models import Add_Friend

response = {}
# Create your views here.
def index(request):
	response['form'] = Add_Friend_Form
	fren = Add_Friend.objects.all()
	response['fren'] = fren
	html = 'add_friend/add_friend.html'
	response['add_friend_form'] = Add_Friend_Form
	return render(request, html, response)
	
def add_friend(request):
	form = Add_Friend_Form(request.POST or None)
	if(request.method == 'POST' and form.is_valid()):
		response['name'] = request.POST['name'] if request.POST['name'] != "" else "Anonymous"
		response['url'] = request.POST['url'] if request.POST['url'] != "" else "Anonymous"
		message = Add_Friend(name=response['name'], url=response['url'])
		message.save()
		return HttpResponseRedirect('/friend/')
	else:
		return HttpResponseRedirect('/friend/')
		
