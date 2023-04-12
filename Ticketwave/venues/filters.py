from .models import Venue
from django_filters import rest_framework as filters

class venueFilter(filters.FilterSet):
    
    class Meta:
        model = Venue
        
        fields = {
            'id': ['exact', 'in'],
            'name': ['exact'],
            'country': ['exact'],
            'city': ['exact'],
            'state': ['exact'],
            'address': ['exact'],
            'latitude': ['gte', 'lte'],
            'longitude': ['gte', 'lte'],
            'event': ['exact', 'in'],
            'event__capacity': ['exact', 'gte', 'lte'],
        }
        #date range example ?created_at__gte=2022-01-01&created_at__lte=2022-01-31
        
