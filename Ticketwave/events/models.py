from django.db import models
from discounts.models import Discounts

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=80)
    summary = models.TextField()
    description = models.TextField()
    url = models.URLField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True) # changes automatically as added
    changed = models.DateTimeField(auto_now=True) # changes automatically as saved
    status = models.TextField()
    online_event = models.BooleanField()
    hide_start_date = models.BooleanField()
    hide_end_date = models.BooleanField()
    discounts = models.ManyToOneRel(Discounts.event_id)
    