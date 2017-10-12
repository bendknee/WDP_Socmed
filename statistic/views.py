from django.shortcuts import render
from update_status.models import Status
import profile_page.views as profile

response = {}

def index(request):
    response['name'] = profile.response['author']
    response['birthday'] = profile.birthday
    response['email'] = profile.email
    response['friends'] = '21' #len(ModelsTirta.objects.all())
    response['feeds'] = Status.objects.count()
    if Status.objects.count() > 0:
        response['last_feed'] = Status.objects.all()[Status.objects.count()-1:]
    else:
        response['last_feed'] = "No Posts Yet!"
    html = 'statistic/statistic.html'
    return render(request, html, response)
