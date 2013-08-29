from django.shortcuts import render
from .models import Country

#TODO
#from .models import States
#from .models import County
#from .models import Course


#Landing page needs a list of [available] [countries]
def country_list(self, request, *args, **kvargs):
    '''
        This functions returns a list of available countries and
        will eventually links them to the states/provinces/territories
        associated with them.
    '''
    
    #Get Countries
    country_list = Country.objects.filter(available=True)
    #Template
    template_name = "countries_landing.html"
    
    #Context
    context = {
        "country_list": country_list
    }
    
    return render(request, template_name, context)

