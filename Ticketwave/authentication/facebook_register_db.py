from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
import os


app_id = 'YOUR_FACEBOOK_APP_ID' #os.environ.get('FACEBOOK_APP_ID')
secret_key = 'YOUR_FACEBOOK_SECRET_KEY' #os.environ.get('FACEBOOK_SECRET_KEY')

# Get the current site
current_site = Site.objects.get_current()

# Create a new social application for the Facebook provider
facebook_app = SocialApp.objects.create(
    provider='facebook',
    name='Facebook',
    client_id=app_id,
    secret=secret_key
)

# Associate the social application with the current site
facebook_app.sites.add(current_site)