from django.shortcuts import render

from core import models

def index(request):
	
	template = 'dashboard/index.html'
	context = {
		'systems': models.System.objects.filter(active=True),
		'current_incidents': models.Incident.objects.filter(closed__isnull=True),
		'past_incidents': models.Incident.objects.filter(closed__isnull=False),
	}
	return render(request, template, context)