#
#@author ryan wallner
#email:  wallnerryan@gmail.com
#
#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyp.views.home', name='home'),
    # url(r'^cyp/', include('cyp.foo.urls')),
    
    #Home
    url(r'^$', views.LandingPageView.as_view(), name="home"),
    
    #Lessons
    #Other Lessons URLS are in lessons/urls.py
    url(r'^lessons/', include('lessons.urls', namespace="lessons")),

    #Router to Admin Interface
    url(r'^admin/', include(admin.site.urls)),
)