# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from apps_gallery.core.models import App, Tag, Developer

def index(request):
    if request.method == 'GET':
        apps = App.objects.all()
        render_var = {
            'host': request.get_host(),
            'apps': apps,
        }
        return render_to_response('index.html', render_var)
    
def about(request):
    if request.method == 'GET':
        return render_to_response('about.html')
    
def howtosubmit(request):
    if request.method == 'GET':
        return render_to_response('howtosubmit.html')
