from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout as logout_user, login as login_user
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def login(request):
	if request.user.is_authenticated():
		messages.info(request, 'You are already logged in.')

		if request.GET.get('next'):
			return redirect(request.GET.get('next'))
		else:
			return redirect(reverse('manager_index'))

	if request.POST:
		user = request.POST.get('username')
		pawd = request.POST.get('password')

		print user, pawd

		user = authenticate(username=user, password=pawd)

		if user is not None:
			if user.is_active:
				login_user(request, user)
				messages.info(request, 'Login successful.')

				if request.GET.get('next'):
					return redirect(request.GET.get('next'))
				else:
					return redirect(reverse('manager_index'))
			else:
				messages.add_message(request, messages.ERROR, 'User account is not active.')
		else:
			messages.add_message(request, messages.ERROR, 'Account not found with those details.')

	context = {}
	template = 'login.html'

	return render(request, template, context)

@login_required
def logout(request):
	messages.info(request, 'You have been logged out.')
	logout_user(request)
	return redirect(reverse('login'))