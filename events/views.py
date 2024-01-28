from django.shortcuts import render, get_object_or_404

from .models import Event

def show_events(request):
    events = Event.objects.all()  
    return render(request, 'event_list.html', {'events': events})

def event_details(request,id):
    event=get_object_or_404(Event,id=id)
    return render(request,'event_details.html', {'event':event})


