
from .models import Country, GeoMap
from django.views.generic import ListView, TemplateView, DetailView

#TODO
#from .models import States
#from .models import County
#from .models import Course

#Mixin allows us to consolidate 'available on queries"
class AvailableMixin(object):
    def get_queryset(self):
        queryset = super(AvailableMixin, self).get_queryset()
        return queryset.filter(available=True)
    

class LessonsLanding(TemplateView):
    template_name = "lessons/lessons.html"
    
class CountryList(AvailableMixin,ListView):
    model = Country
    
class GeoMapView(AvailableMixin,DetailView):
    model  = GeoMap
    template_name = "lessons/geo_map.html"
    context_object_name = "gmap"
