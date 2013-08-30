#
#@author ryan wallner
#email:  wallnerryan@gmail.com
#
#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    #Lessons
    url(r'^$', views.LessonsLanding.as_view(), name="landing"),
    
    #Countries
    url(r'^countries/$', views.CountryList.as_view(), name="list"),
)