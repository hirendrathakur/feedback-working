from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'feedback.views.home', name='home'),
    url(r'^feedback/', include('feedback.urls', namespace="feedback")),
    url(r'^getmail/', 'feedback.views.getmail', name='getmail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^instructions/$', 'feedback.views.instruction', name='instruction'),)
