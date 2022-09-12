from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.
def index(request):
    event = Event.objects.first()
    event_name = event.name
    event_icon = event.icon
    event_description = event.description
    event_start = event.event_start
    print(f'{event_start}')
    return render(request, 'index.html',
    context={'event_name':event_name,'event_icon':event_icon,'event_description':event_description,'event_start':event_start})
