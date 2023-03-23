from django.db import models
from django.contrib.auth.models import AbstractUser
class users(AbstractUser):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=80)
  first_name=models.CharField(max_length=80)
  last_name=models.CharField(max_length=80)
  is_public=models.BooleanField(default=True)
  image_id=Models.CharField(max_length=200)
  pass
class users_emails(models.Model):
  user_id=models.ForeignKey(users,to_field='id')
  email=models.CharField(max_length=80)
  verified=models.BooleanField(default=False)
  pass
