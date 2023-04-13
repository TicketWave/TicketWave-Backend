from django.contrib.sites.models import Site

# Replace these values with your own site domain and name
site_domain = '127.0.0.1:8000'
site_name = 'ticketwave'

# Get the current site
current_site = Site.objects.get_current()

# Update the current site's domain and name
current_site.domain = site_domain
current_site.name = site_name
current_site.save()