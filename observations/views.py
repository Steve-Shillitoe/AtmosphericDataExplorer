from django.shortcuts import render

from .models import Observation

def observation_list(request):
    # Get all observations from the database, newest first
    observations = Observation.objects.order_by('-timestamp')
    
    # Render the template with observations
    return render(request, 'observations/list.html', {"observations": observations})

