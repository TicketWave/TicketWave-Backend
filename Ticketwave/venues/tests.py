from django.test import TestCase
from geopy.geocoders import Nominatim

# Create your tests here.

class VenueTestCase(TestCase):
    def test_IncrementView_Serizalizer(self):
        geolocator = Nominatim(user_agent="ticketwave")
        location = geolocator.reverse(f'48.858093, 2.294694')
        address = location.raw['address']
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
        self.assertEqual(state, 'Île-de-France')
        self.assertEqual(city,'Paris' )
        self.assertEqual(country, 'France')