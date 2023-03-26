from django.db import models

# Create your models here.


class TicketClass(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
 
    def __str__(self) -> str:
<<<<<<< HEAD
        return self.name
    
=======
        return self.name
>>>>>>> a9e624436dab9ba50216ee07b87c0a3a10f22ce0
