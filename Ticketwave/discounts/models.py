from django.db import models
from events.models import Event

class Discounts(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, blank=False, max_length=20)
    type = models.CharField(max_length=255)
    end_date = models.DateTimeField(blank=False)
    start_date = models.DateTimeField(blank=False)
    percent_off = models.FloatField()
    quantity_available = models.IntegerField()
    quantity_sold = models.IntegerField()
    # event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_id = models.IntegerField(default=-1)
    