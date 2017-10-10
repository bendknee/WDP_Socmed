from django.shortcuts import render

response = {}

def index(request):
    response['friends'] = None #len(ModelsTirta.objects.all())
    feeds = None #ModelsMiki.objects.all()
    response['feeds'] = None #len(feeds)
    response['last_feed'] = None #ModelsMiki.objects.get(pk=len(feeds)-1)
    html = 'statistic/statistic.html'
    render(request, html, response)
