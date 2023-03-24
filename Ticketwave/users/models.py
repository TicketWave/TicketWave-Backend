from django.db import models
from django.contrib.auth.models import AbstractUser
from media.models import Media

class Users(AbstractUser):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=80)
  first_name = models.CharField(max_length=80)
  last_name = models.CharField(max_length=80)
  is_public = models.BooleanField(default=True)
  image_id = models.ForeignKey(to= Media, on_delete=models.PROTECT)

class Users_emails(models.Model):
  user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
  email = models.CharField(max_length=80)
  verified = models.BooleanField(default=False)
