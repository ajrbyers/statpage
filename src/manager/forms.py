from django import forms
from core import models

class NewSystem(forms.ModelForm):

	class Meta:
		model = models.System
		exclude = ()

class Incident(forms.ModelForm):

	class Meta:
		model = models.Incident
		exclude = ('notes', 'user', 'started', 'closed')

class Note(forms.ModelForm):

	class Meta:
		model = models.Note
		fields = ('text',)