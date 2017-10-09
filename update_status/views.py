from django.shortcuts import render

# Create your views here.

response = {}
def index(request):
    response['author'] = 'Kelompok 11'
    html = 'update_status/status.html'
    return render(request,html,response)
