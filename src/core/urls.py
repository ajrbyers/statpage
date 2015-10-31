from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^manager/', include('manager.urls')),

    # Core URLS
    url(r'^$', 'dashboard.views.index', name='index'),
    url(r'^login/$', 'core.views.login', name='login'),
    url(r'^logout/$', 'core.views.logout', name='logout'),
]
