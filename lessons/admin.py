#
#@author ryan wallner
#email:  wallnerryan@gmail.com
#
from django.contrib import admin
#Import the models needed for admin
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    #Change what an admin sees for easier visual
    fields = ("name", "available", "flag")
    list_display = ["name", "available", "flag"]
    list_display_links = ["name"]
    list_editable = ["available"]
    list_filter =  ["available"]


#Add the Country Model to the Admin Site
admin.site.register(Country, CountryAdmin)