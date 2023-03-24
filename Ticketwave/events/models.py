from django.db import models

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
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

class Event_private(models.Model):
    listed = models.BooleanField()
    shareable = models.BooleanField()
    invite_only = models.BooleanField()
    show_remaining = models.BooleanField()
    password = models.TextField()
    capacity = models.IntegerField()
    capacity_is_custom = models.BooleanField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE) # once event is deleted, the private model is automatically deleted