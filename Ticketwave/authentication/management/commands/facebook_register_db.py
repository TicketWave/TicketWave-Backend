from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Creates a new social application for the Facebook provider'

    def handle(self, *args, **options):
        app_id = os.environ.get('FACEBOOK_APP_ID')
        secret_key = os.environ.get('FACEBOOK_APP_SECRET_KEY')

        # Get the current site
        current_site = Site.objects.get_current()
        try:
            # Create a new social application for the Facebook provider
            facebook_app = SocialApp.objects.create(
                provider='facebook',
                name='Facebook',
                client_id=app_id,
                secret=secret_key
            )

            # Associate the social application with the current site
            facebook_app.sites.add(current_site)

            self.stdout.write(self.style.SUCCESS('Successfully created a new social application for the Facebook provider'))
        except:
            self.stdout.write(self.style.ERROR('error might already created or other error'))