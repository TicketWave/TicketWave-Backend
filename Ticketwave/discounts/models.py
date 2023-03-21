from django.db import models
from events.models import Event

class Discounts(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, blank=False)
    type = models.CharField()
    end_date = models.DateTimeField(blank=False)
    start_date = models.DateTimeField(blank=False)
    percent_off = models.FloatField()
    quantity_available = models.IntegerField()
    quantity_sold = models.IntegerField()
    event_id = models.OneToOneField(to=Event.discounts)
    