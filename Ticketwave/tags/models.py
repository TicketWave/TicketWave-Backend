from django.db import models
from events.models import Event

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=80)
    tags = models.ManyToManyField(Event, on_delete=models.CASCADE, related_name='tags')
    
    def __str__(self) -> str:
        return self.name