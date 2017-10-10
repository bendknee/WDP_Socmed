from django.shortcuts import render
from .forms import Status_Form

# Create your views here.

response = {}
def index(request):
    response['status_form'] = Status_Form
    html = 'update_status/status.html'
    return render(request,html,response)
