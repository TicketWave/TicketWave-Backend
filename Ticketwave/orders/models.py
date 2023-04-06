from django.db import models

from events.models import Event
from users.models import Users
# Create your models here.

class Order(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    promo_code = models.TextField(null=True)
    status = models.TextField(blank=True)
    cost = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True) # changes automatically as added
    #message_on_confirmation = models.TextField(null=True)
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='order') 
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='order') 
    
    def __str__(self):
        return self.first_name + self.last_name