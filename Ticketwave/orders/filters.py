from .models import Order
from django_filters import rest_framework as filters

class orderfilter(filters.FilterSet):
    
    class Meta:
        model = Order
        
        fields = {
            'created': ['exact', 'gte', 'lte'],
            'first_name': ['exact'],
            'last_name': ['exact'],
            'email': ['exact'],
            'cost': ['exact'],
            'user': ['exact'],
            'event': ['exact'],
            'cost': ['exact', 'gte', 'lte'],
        }
        #date range example ?created_at__gte=2022-01-01&created_at__lte=2022-01-31
        