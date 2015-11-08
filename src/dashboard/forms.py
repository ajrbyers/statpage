from django import forms
from core import models

class NewSub(forms.ModelForm):

	class Meta:
		model = models.Subscriber
		exclude = ('confirmation_code', 'confirmed')