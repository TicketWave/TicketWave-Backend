from django.db import models

# Create your models here.
class Venue(models.Model):
    
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    #age_restriction= models.BooleanField(default=False) #already represented in the event itself
    #capacity = models.IntegerField() #already represented in the event itself