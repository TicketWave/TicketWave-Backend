from django.db import models
from django.contrib.auth.models import AbstractUser
class Users(AbstractUser):
  name=models.StringField
  first_name=models.StringField
  last_name=models.C
  is_public=models.BooleanField(default=True)
  image_id=Models.StringField
  pass
