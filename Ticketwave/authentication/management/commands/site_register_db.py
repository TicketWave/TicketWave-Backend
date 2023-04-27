from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = 'Updates the current site domain and name'

    def handle(self, *args, **options):
        # Replace these values with your own site domain and name
        site_domain = 'ticketwave.me'
        site_name = 'ticketwave'

        # Get the current site
        current_site = Site.objects.get_current()

        # Update the current site's domain and name
        current_site.domain = site_domain
        current_site.name = site_name
        current_site.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated site domain and name'))