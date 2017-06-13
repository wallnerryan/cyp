#
#@author ryan wallner
#email:  wallnerryan@gmail.com
#
from django.db import models
from django.template.defaultfilters import slugify
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
#But using this Model so the option to expand exists
class Country(models.Model):
    #Filename of the Country Flag Image
    def get_flag_image(self, filename):
        return u"%s" % filename
    
    #We will only support the United States of America right now.
    name = models.CharField(unique=True,max_length=255)
    flag = models.ImageField(upload_to=get_flag_image)
    available = models.BooleanField(default=True)
    #Acts as unique foreignkey for GeoMap
    gmap = models.CharField(unique=True, max_length=5)
    slug = models.SlugField(max_length=255, blank=True, default='')
    
    #Alphabetic Ordering
    class Meta:
        ordering = ["name"]
    
    
    #Represent the Country via their NAME
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kvargs ):
         if not self.slug:
            self.slug = slugify(self.name).lower()
         super(Country, self).save(*args, **kvargs)
        
#The name coordinates to map type, USA supported first
class GeoMap(models.Model):
    name = models.CharField(unique=True,max_length=255)
    available = models.BooleanField(default=True)
    #Map GeoMap's foreignkey to map of Country
    country = models.ForeignKey(Country, to_field='gmap')
    slug = models.SlugField(max_length=255, blank=True, default='')
    
    #Alphabetic Ordering
    class Meta:
        ordering = ["name"]
    
    #Represent the Country via their NAME
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kvargs ):
        if not self.slug:
            #This is the foreign key gmap, e.g "usa" for Country United States
            self.slug = slugify(self.country).lower()
        super(GeoMap, self).save(*args, **kvargs)
    

#Need the states (for US only)
class State(models.Model):
    name = models.CharField(unique=True,max_length=255)
    available = models.BooleanField(default=True)
    #Map the map to foreignkey of geo_map for state
    geo_map = models.ForeignKey(GeoMap, to_field='name')
    slug = models.SlugField(max_length=255, blank=True, default='')
    
     #Alphabetic Ordering
    class Meta:
        ordering = ["name"]
    
    #Represent the Country via their NAME
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kvargs ):
        if not self.slug:
            self.slug = slugify(self.name).lower()
        super(GeoMap, self).save(*args, **kvargs)

#Need the states (for US only)
class County(models.Model):
    name = models.CharField(unique=True,max_length=255)
    available = models.BooleanField(default=True)
    #Map the state owned by the county to the state foreignkey
    state = models.ForeignKey(State, to_field='name')
    slug = models.SlugField(max_length=255, blank=True, default='')
    
     #Alphabetic Ordering
    class Meta:
        ordering = ["name"]
    
    #Represent the Country via their NAME
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kvargs ):
        if not self.slug:
            self.slug = slugify(self.name).lower()
        super(GeoMap, self).save(*args, **kvargs)
        
#TODO GolfCourse
#TODO Somehow map Pros, to GolfCourse, need Pros infrastructure next.
    



