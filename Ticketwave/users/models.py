from django.db import models
from django.contrib.auth.models import AbstractUser
class Users(AbstractUser):
  id=models.AutoField(primary_key=True)
  first_name=models.CharField(max_length=80)
  last_name=models.CharField(max_length=80)
  is_public=models.BooleanField(default=True)
  image_id=Models.CharField(max_length=200)
  pass
