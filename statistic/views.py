from django.shortcuts import render

response = {}

def index(request):
    response['name'] = 'Musibah Smith'
    response['friends'] = '21' #len(ModelsTirta.objects.all())
    feeds = None #ModelsMiki.objects.all()
    response['feeds'] = '2119' #len(feeds)
    response['last_feed'] = 'hehe AHHHHHHH' #ModelsMiki.objects.get(pk=len(feeds)-1)
    html = 'statistic/statistic.html'
    return render(request, html, response)
