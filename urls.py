#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyp.views.home', name='home'),
    # url(r'^cyp/', include('cyp.foo.urls')),

    #Router to Admin Interface
    url(r'^admin/', include(admin.site.urls)),
)
