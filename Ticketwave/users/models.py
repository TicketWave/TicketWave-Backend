from django.db import models
from django.contrib.auth.models import AbstractUser
from media.models import Media

class Users(AbstractUser):
  is_public = models.BooleanField(default=True)
  image_id = models.IntegerField()
