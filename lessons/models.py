#
#@author ryan wallner
#email:  wallnerryan@gmail.com
#
from django.db import models

# These models will outline the data involved in searching for a lesson
# e.g. Country, State, County, Golf Course and relate them to lessons available
# from the pros listed at that specific course.
#
# Models
#  -
#
#TODO create country model and reference
#TODO create province, territory, states of other countries.

#Focusing on "USA" "United States of America" for lessons


class Country(models.Model):
    #Filename of the Country Flag Image
    def get_flag_image(self, filename):
        return u"%s" % filename
    
    #We will only support the United States of America right now.
    name = models.CharField(unique=True,max_length=255)
    flag = models.ImageField(upload_to=get_flag_image)
    available = models.BooleanField(default=True)
    
    #Alphabetic Ordering
    class Meta:
        ordering = ["name"]
    
    
    #Represent the Country via their NAME
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kvargs ):
        super(Country, self).save(*args, **kvargs)
        

    
    