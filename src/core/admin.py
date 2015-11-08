from django.contrib import admin
from models import *

class SystemAdmin(admin.ModelAdmin):
	list_display = ('name', 'active')
	list_filter = ('active',)
	search_fields = ('name',)

class NoteAdmin(admin.ModelAdmin):
	list_display = ('posted',)
	list_filter = ('posted',)
	search_fields = ('description',)

class IncidentAdmin(admin.ModelAdmin):
	list_display = ('system', 'status', 'started', 'closed', 'user')
	list_filter = ('system', 'status', 'user')

class SubscriberAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email_address')
	list_filter = ('first_name', 'last_name', 'email_address')

admin_list = [
	(System, SystemAdmin),
	(Note, NoteAdmin),
	(Incident, IncidentAdmin),
	(Subscriber, SubscriberAdmin),
]

[admin.site.register(*t) for t in admin_list]
