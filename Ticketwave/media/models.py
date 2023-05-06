from django.db import models
from events.models import Event


# Create your models here.

class Media(models.Model):
    id=models.IntegerField(unique=True, blank=False, max_length=100, primary_key= True)
    page_place = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    width = models.IntegerField()
    height = models.IntegerField()
    topleft_crop_x = models.IntegerField()
    topleft_crop_y = models.IntegerField()
    
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.url
