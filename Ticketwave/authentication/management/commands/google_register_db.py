from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Creates a new social application for the Google provider'

    def handle(self, *args, **options):
        client_id = os.environ.get('GOOGLE_CLIENT_ID') 
        secret_key = os.environ.get('GOOGLE_SECRET_KEY')
        try:
            # Get the current site
            current_site = Site.objects.get_current()

            # Create a new social application for the Google provider
            google_app = SocialApp.objects.create(
                provider='google',
                name='Google',
                client_id=client_id,
                secret=secret_key
            )

            # Associate the social application with the current site
            google_app.sites.add(current_site)

            self.stdout.write(self.style.SUCCESS('Successfully created a new social application for the Google provider'))
        except:
            self.stdout.write(self.style.ERROR('error might already created or other error'))