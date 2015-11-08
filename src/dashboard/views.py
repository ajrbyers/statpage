from uuid import uuid4

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings

from core import models, email
from dashboard import forms

def index(request):
	
	template = 'dashboard/index.html'
	context = {
		'systems': models.System.objects.filter(active=True),
		'current_incidents': models.Incident.objects.filter(closed__isnull=True),
		'past_incidents': models.Incident.objects.filter(closed__isnull=False),
	}
	return render(request, template, context)

def new_subscriber(request):

	form = forms.NewSub()

	if request.POST:
		form = forms.NewSub(request.POST)
		if form.is_valid():
			new_sub = form.save(commit=False)
			new_sub.confirmation_code = uuid4()
			new_sub.save()

			email_context = {
				'subscriber': new_sub,
				'settings': settings,
				'accept_url': '%s/dashboard/subscribe/%s/accept/' % (settings.BASE_URL, new_sub.confirmation_code),
				'decline_url': '%s/dashboard/subscribe/%s/decline/' % (settings.BASE_URL, new_sub.confirmation_code),
			}

			email.send_email(new_sub.email_address, 'Status Subscription', email_context, 'email_subscribe.html')
			messages.add_message(request, messages.SUCCESS, 'You are now subscribed to notifications.')

			return redirect(reverse('dashboard_index'))

	template = 'dashboard/new_subscriber.html'
	context = {
		'form': form,
	}
	return render(request, template, context)

def handle_subscription_activation(request, code, action):

	subscription = get_object_or_404(models.Subscriber, confirmation_code=code)

	if action == 'accept':
		subscription.confirmed = True
		subscription.confirmation_code = None
		subscription.save()
		message = 'Subscription confirmed.'
	elif action == 'decline':
		subscription.delete()
		message = 'Record removed.'

	messages.add_message(request, messages.SUCCESS, message)
	return redirect(reverse('dashboard_index'))





