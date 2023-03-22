from django.db import models

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    short_name = models.CharField(max_length=18, unique=True)
    resource_uri = models.URLField(blank=True, null=True)
    parent_category = models.IntegerField(blank=True, null=True)
