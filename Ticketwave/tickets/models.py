from django.db import models
from events.models import Event
from users.models import Users
# Create your models here.


class Ticket(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # user and event will be replaced with foreign key field later 
    price = models.FloatField()
    SalesStart = models.DateTimeField()
    StartTime = models.DateTimeField()
    SalesEnd = models.DateTimeField()
    EndTime = models.DateTimeField()
    CodeName = models.CharField(max_length=255)
    RevealHidden = models.BooleanField()
    Discount = models.FloatField()
    PromoStart = models.DateTimeField()
    PromoEnds = models.DateTimeField()
    ApplyCode = models.BooleanField()
    TicketLimit = models.SmallIntegerField()
    #CSVfile = models.FileField() # 
    amount = models.PositiveIntegerField()
    #TicketList = 
    State = models.CharField(max_length=255)
    Capacity = models.IntegerField()
 
    def __str__(self) -> str:   # when one calls ticket models with any entity, returns its name
        return self.name
