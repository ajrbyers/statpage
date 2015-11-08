from django.db import models
from django.contrib.auth.models import User

def status_choices():
	return (
		('operational', 'Operational'),
		('partial_outage', 'Partial Outage'),
		('major_outage', 'Major Outage'),
	)

class System(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return u'%s' % (self.name)

	def open_incidents(self):
		return Incident.objects.filter(system=self, closed__isnull=True)

class Note(models.Model):
	text = models.TextField()
	posted = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-posted']

	def __unicode__(self):
		return u'Note: %s' % (self.posted)

class Incident(models.Model):
	system = models.ForeignKey(System)
	status = models.CharField(max_length=100, choices=status_choices())
	notes = models.ManyToManyField(Note)

	started = models.DateTimeField(null=True, blank=True)
	closed = models.DateTimeField(null=True, blank=True)
	user = models.ForeignKey(User)

	class Meta:
		ordering = ['-started']

	def __unicode__(self):
		return u'%s %s' % (self.system.name, self.status)
