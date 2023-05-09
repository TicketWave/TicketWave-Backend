from django.db import models
from events.models import Event
from discounts.models import Discounts

# Create your models here.


class Ticket(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # user and event will be replaced with foreign key field later
    price = models.FloatField()
    SalesStart = models.DateTimeField()
    StartTime = models.DateTimeField()
    SalesEnd = models.DateTimeField()
    EndTime = models.DateTimeField()
    RevealHidden = models.BooleanField()
    Discount = models.ForeignKey(Discounts, on_delete=models.CASCADE, blank=True)
    PromoStart = models.DateTimeField(blank=True)
    PromoEnds = models.DateTimeField(blank=True)
    ApplyCode = models.BooleanField()
    TicketLimit = models.SmallIntegerField()
    # CSVfile = models.FileField() #
    amount = models.PositiveIntegerField(blank=True)
    # TicketList =
    State = models.CharField(max_length=255, blank=True)
    Capacity = models.IntegerField()

    def __str__(
        self,
    ) -> str:  # when one calls ticket models with any entity, returns its name
        return self.name
