from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
import os


client_id = '584138943946-lbr8f7p9rkf62eao96dorqb3v8p5q3io.apps.googleusercontent.com' #os.environ.get('GOOGLE_APP_ID')
secret_key = 'the old leaked ones are deleted and new ones were made, don"T worry lol' #os.environ.get('GOOGLE_SECRET_KEY')

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