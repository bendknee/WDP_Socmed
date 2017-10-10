from django.shortcuts import render

response = {}

def index(request):
    response['friends'] = None #len(ModelsTirta.objects.all())
    response['feeds'] = None #len(ModelsMiki.objects.all())
    response['last_feed'] = None #ModelsMiki.
    html = 'statistic/statistic.html'
    render(request, html, response)
