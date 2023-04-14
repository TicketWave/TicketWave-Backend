from geopy.geocoders import Nominatim

def get_location_info(latitude, longitude):
    geolocator = Nominatim(user_agent="ticketwave") #geoapiExercises
    location = geolocator.reverse(f'{latitude}, {longitude}')
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return city, state, country