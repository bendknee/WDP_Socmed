from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Status_Form

# Create your views here.

response = {}
def index(request):
    response['status_form'] = Status_Form
    html = 'update_status/status.html'
    return render(request,html,response)

def update_status(request):
    return HttpResponseRedirect('/status/')
