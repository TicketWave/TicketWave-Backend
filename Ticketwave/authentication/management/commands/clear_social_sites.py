from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Clears all social apps'

    def handle(self, *args, **options):
        
        try:
            # Delete all objects in the SocialApp table
            SocialApp.objects.all().delete()        
            self.stdout.write(self.style.SUCCESS('cleared social providers table'))
            
        except:
            self.stdout.write(self.style.ERROR('An error occurred'))