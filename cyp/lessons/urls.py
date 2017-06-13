#
#@author ryan wallner
#email:  wallnerryan@gmail.com
#
#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, include, url
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    #Lessons
    url(r'^$', views.LessonsLanding.as_view(), name="landing"),
    
    #Countries
    url(r'^countries/$', views.CountryList.as_view(), name="list"),
    
    #Dig down to GeoMap (gmap is 3-5 char field)
     url(r'^countries/(?P<slug>((([a-z]+)([-])?)+)$)',
         views.GeoMapView.as_view(),name="geo"),   
)

urlpatterns += staticfiles_urlpatterns()
