from django.db import models
from users.models import Users

class Attendees(models.Model):
  attendee_id= models.AutoField(primary_key=True)
  created= models.DateTimeField()
  changed= models.DateTimeField()
  quantity= models.IntegerField()
  costs= models.FloatField()
  checked_in= models.BooleanField()
  cancelled= models.BooleanField()
  refunded= models.BooleanField()
  address= models.CharField(max_length=255)
  delivery_method= models.CharField(max_length=255)
  base_price= models.FloatField()
  ticketwave_fee= models.FloatField()
  tax= models.FloatField()
  payment_fee= models.FloatField()
  gross= models.FloatField()
  user_id= models.ForeignKey(Users, on_delete=models.CASCADE, default = 1)
