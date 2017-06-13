#
#@author ryan wallner
#email:  wallnerryan@gmail.com
#
from django.contrib import admin
#Import the models needed for admin
from .models import Country, GeoMap

class CountryAdmin(admin.ModelAdmin):
    #Change what an admin sees for easier visual
    fields = ("name", "available", "flag", "gmap")
    list_display = ["name", "available", "flag", "gmap"]
    list_display_links = ["name"]
    list_editable = ["available"]
    list_filter =  ["available"]
    
class GeoMapAdmin(admin.ModelAdmin):
    #Change what an admin sees for easier visual
    fields = ("name", "available", "country")
    list_display = ["name", "available", "country"]
    list_display_links = ["name"]
    list_editable = ["available"]
    list_filter =  ["available"]


#Add the Country Model to the Admin Site
admin.site.register(Country, CountryAdmin)
admin.site.register(GeoMap, GeoMapAdmin)