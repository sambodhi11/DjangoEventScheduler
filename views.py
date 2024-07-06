from django.http import HttpResponse # type: ignore
from django.shortcuts import render , redirect
from django.db import IntegrityError 
from Event.models import Event
from .forms import EventForm 


def index(request):
    return render(request, 'index.html')

def add(request):
    context = {"data": Event.objects.all()}
    
    if request.method == 'POST':
        events_name = request.POST.get('Eventname')
        events_date = request.POST.get('EventDate')
        events_time = request.POST.get('EventTime')
        events_description = request.POST.get('EventDescription')
    

        if not events_name or not events_date or not events_time or not events_description:
            context['error'] = "All fields are required."
            return render(request, 'add.html', context)
        
        try:
            new_event = Event(name=events_name, date=events_date, time=events_time, description=events_description)
            new_event.save()
            context['message'] = "Event added ."
        except IntegrityError:
            context['error'] = "Error adding the event. Please try again."
            return render(request, 'add.html', context)
        return HttpResponse("DATA ADDED")
    return render(request, 'add.html', context) 
    
def Update(request):
    if request.method == 'POST':
        name = request.POST.get('Eventname')
        date = request.POST.get('EventDate')
        time = request.POST.get('EventTime')
        description = request.POST.get('EventDescription')

        try:
            
            event = Event.objects.get(name=name)
            if date:
                event.date = date
            if time:
                event.time = time
            if description:
                event.description = description
            event.save()

            return redirect('display')  
        except Event.DoesNotExist:
            error = "Event does not exist."
            return render(request, 'Update.html', error)

    return render(request, 'Update.html')
    

def display(request):
    events = Event.objects.all()
    return render(request, 'display.html', {'events': events})

        
def delete(request):
    if request.method == 'POST':
        name = request.POST.get('Eventname')  # Assuming Eventname is used for deletion
        try:
            event = Event.objects.get(name=name)
            event.delete()
            return redirect('display')  # Redirect to display page after deletion
        except Event.DoesNotExist:
            error = "Name does not exist."
            
            return render(request, 'delete.html', {'error': error})
        return HttpResponse("DATA ADDED")
    return render(request, 'delete.html')