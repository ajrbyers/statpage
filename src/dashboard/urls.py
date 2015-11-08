from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'dashboard.views.index', name='dashboard_index'),
    url(r'^subscribe/$', 'dashboard.views.new_subscriber', name='new_subscriber'),
    url(r'^subscribe/(?P<code>[-\w./]+)/(?P<action>[-\w./]+)/$', 'dashboard.views.handle_subscription_activation', name='handle_subscription_activation'),

]
