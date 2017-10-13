from django.shortcuts import render
from django.http import HttpResponseRedirect
from profile_page.views import response as resp
from .forms import Status_Form
from .models import Status

# Create your views here.

response = {}
def index(request):
    response['status_form'] = Status_Form
    response['status'] = Status.objects.all()[::-1]
    response['name'] = resp['author']
    html = 'update_status/status.html'
    return render(request,html,response)

def update_status(request):
    form = Status_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        status = request.POST['status']
        status = Status(status = status)
        status.save()
    return HttpResponseRedirect('/status/')
