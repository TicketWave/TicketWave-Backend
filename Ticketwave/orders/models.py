from django.db import models

from events.models import Event
from users.models import Users
from attendees.models import Attendees
# Create your models here.


class Order(models.Model):
    
    status_choices = [
        ('started', 'started'),
        ('pending', 'pending'),
        ('placed', 'placed'),
        ('abandoned', 'abandoned'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    promo_code = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=16, default='pending', choices=status_choices)
    cost = models.IntegerField()
    # changes automatically as added
    created = models.DateTimeField(auto_now_add=True)
    # message_on_confirmation = models.TextField(null=True)

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='order')
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='order')
    attendee = models.ForeignKey(
        Attendees, on_delete=models.CASCADE, related_name='order')

    def __str__(self):
        return self.first_name + self.last_name
