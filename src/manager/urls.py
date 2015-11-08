from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'manager.views.index', name='manager_index'),
    
    url(r'^system/new/$', 'manager.views.system', name='new_system'),
    url(r'^system/(?P<system_id>\d+)/$', 'manager.views.system', name='edit_system'),

    url(r'^indcident/new/$', 'manager.views.incident', name='new_incident'),
    url(r'^note/(?P<incident_id>\d+)/close/$', 'manager.views.close_incident', name='close_incident'),
    url(r'^system/(?P<incident_id>\d+)/$', 'manager.views.incident', name='edit_incident'),

    url(r'^note/(?P<incident_id>\d+)/$', 'manager.views.add_new_note', name='add_new_note'),

]
