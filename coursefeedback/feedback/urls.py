__author__ = 'HIRENDRA'

from django.conf.urls import patterns, url

from feedback import views

urlpatterns = patterns('',
                       url(r'^(?P<key>\w+)/$',views.index, name='index'),
                       url(r'^getmail/$',views.getmail, name='getmail'),
                       url(r'^(?P<prof_pk>\d+)/(?P<stud_roll>\w+)/(?P<sub_pk>\d+)/(?P<key>\w+)/$',views.polls, name='polls'),
                       url(r'^analyse/$',views.analyse, name='analyse'),
                       url(r'^analyse/(?P<prof_pk>\d+)/$',views.courseanalyse, name='courseanalyse'),
                        )