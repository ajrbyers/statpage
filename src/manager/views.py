from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone

from core import models
from manager import forms

@staff_member_required
def index(request):
	
	template = 'manager/index.html'
	context = {
		'systems': models.System.objects.all(),
		'current_incidents': models.Incident.objects.filter(closed__isnull=True),
		'past_incidents': models.Incident.objects.filter(closed__isnull=False),
	}
	return render(request, template, context)

@staff_member_required
def system(request, system_id=None):

	if system_id:
		system = get_object_or_404(models.System, pk=system_id)
		form = forms.NewSystem(instance=system)
	else:
		form = forms.NewSystem()

	if request.POST:
		if system:
			form = forms.NewSystem(request.POST, instance=system)
		else:
			form = forms.NewSystem(request.POST)

		if form.is_valid():
			new_system = form.save()
			if system:
				message = 'System updated.'
			else:
				message = 'System created.'

			messages.add_message(request, messages.ERROR, message)
			return redirect(reverse('manager_index'))

	template = 'manager/system_new.html'
	context = {
		'form': form,
	}
	return render(request, template, context)

@staff_member_required
def incident(request, incident_id=None):

	if incident_id:
		incident = get_object_or_404(models.Incident, pk=incident_id)
		form = forms.Incident(instance=incident)
	else:
		form = forms.Incident()

	if request.POST:
		if incident_id:
			form = forms.Incident(request.POST, instance=insident)
		else:
			form = forms.Incident(request.POST)

		if form.is_valid():
			saved_incident = form.save(commit=False)
			saved_incident.user = request.user
			saved_incident.save()

			if incident_id:
				message = 'Incident updated.'
			else:
				note = request.POST.get('note')
				if note:
					new_note = models.Note(text=note)
					new_note.save()
					saved_incident.notes.add(new_note)
					saved_incident.started = timezone.now()
					saved_incident.save()

				message = 'Incident created.'

			messages.add_message(request, messages.ERROR, message)
			return redirect(reverse('manager_index'))

	template = 'manager/incident.html'
	context = {
		'form': form,
	}
	return render(request, template, context)

@staff_member_required
def add_new_note(request, incident_id):
	incident = get_object_or_404(models.Incident, pk=incident_id)
	form = forms.Note()

	if request.POST:
		form = forms.Note(request.POST)

		if form.is_valid():
			new_note = form.save()
			incident.notes.add(new_note)

			messages.add_message(request, messages.SUCCESS, 'Note added to incident')
			return redirect(reverse('manager_index'))

	template = 'manager/note.html'
	context = {
		'incident': incident,
		'form': form,
	}
	return render(request, template, context)

@staff_member_required
def close_incident(request, incident_id):
	incident = get_object_or_404(models.Incident, pk=incident_id)
	form = forms.Note()

	if request.POST:
		form = forms.Note(request.POST)

		if form.is_valid():
			new_note = form.save()
			incident.notes.add(new_note)
			incident.closed = timezone.now()
			incident.save()

			messages.add_message(request, messages.SUCCESS, 'Note added to incident')
			return redirect(reverse('manager_index'))

	template = 'manager/close_incident.html'
	context = {
		'incident': incident,
		'form': form,
	}
	return render(request, template, context)




