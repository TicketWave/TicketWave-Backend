from django.db import models
from users.models import Users
from orders.models import Order


class Attendees(models.Model):
    attendee_id = models.AutoField(primary_key=True)
    created = models.DateTimeField()
    changed = models.DateTimeField(blank=True)
    quantity = models.IntegerField(blank=True)
    costs = models.FloatField(blank=True)
    checked_in = models.BooleanField()
    cancelled = models.BooleanField()
    refunded = models.BooleanField()
    address = models.CharField(max_length=255, blank=True)
    delivery_method = models.CharField(max_length=255, blank=True)
    base_price = models.FloatField(blank=True)
    ticketwave_fee = models.FloatField(blank=True)
    tax = models.FloatField(blank=True)
    payment_fee = models.FloatField(blank=True)
    gross = models.FloatField(blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
