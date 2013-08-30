
from .models import Country
from django.views.generic import ListView, TemplateView

#TODO
#from .models import States
#from .models import County
#from .models import Course

class LessonsLanding(TemplateView):
    template_name = "lessons/lessons.html"
    
class CountryList(ListView):
    model = Country

    #only available countries
    def get_query_set(self):
        queryset = super(CountryList, self).get_queryset()
        return queryset.filter(available=True)