from .models import Venue
from .serializers import venue_Serializer
from .filters import venueFilter
from .pagination import StandardResultsSetPagination
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.permissions import Is_venueowner
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, AllowAny
from .geolocation import get_location_info


class venue_List(ListAPIView): 
    queryset = Venue.objects.all()
    
    serializer_class = venue_Serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = StandardResultsSetPagination 
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = venueFilter
    search_fields = ['^name'] 
    ordering_fields = ['event__capacity']
    
class venue_Retrieve(RetrieveAPIView):
    queryset = Venue.objects.all()
    serializer_class = venue_Serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class venue_Update(UpdateAPIView):
    queryset = Venue.objects.all()
    lookup_field = 'pk'
    serializer_class = venue_Serializer
    #permission_classes = [IsAuthenticated, Is_venueowner]
    
    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class venue_Destroy(DestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = venue_Serializer
    #permission_classes = [IsAuthenticated, Is_venueowner]

class venue_Create(CreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = venue_Serializer
    #permission_classes = [IsAuthenticated] 
    
    def perform_create(self, serializer):
        name = self.request.data.get('name', None)
        latitude = self.request.data.get('latitude', None)
        longitude = self.request.data.get('longitude', None)
        
        name = self.request.data.get('name', None)
        latitude = self.request.data.get('latitude', None)
        longitude = self.request.data.get('longitude', None)
        
        # Check if name, latitude, and longitude are provided
        if name is None or not latitude is None or not longitude is None:
            return Response({'error': 'Name, latitude, and longitude are required'}, status=400)

        # Check if latitude and longitude are valid
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            return Response({'error': 'Invalid latitude or longitude'}, status=400)
        
        
        city, state, country = get_location_info(latitude, longitude)
        # Clip city, state, and country if necessary
        city = city[:32]
        state = state[:32]
        country = country[:32]
            
        address = f"{city}, {state}, {country}"
            
        # Update the serializer object with the new data
        serializer.validated_data['name'] = name
        serializer.validated_data['city'] = city
        serializer.validated_data['state'] = state
        serializer.validated_data['country'] = country
        serializer.validated_data['address'] = address

        # Validate the serializer object
        serializer.is_valid(raise_exception=True)

        serializer.save()
        
class venue_get_location(APIView):
    def get(self, request):
        try:
            latitude = self.request.data.get('latitude', None)
            longitude = self.request.data.get('longitude', None)
            
            if latitude is None or longitude is None: return Response(status=400)
            
            latitude = float(latitude)
            longitude = float(longitude)
            
            city, state, country = get_location_info(latitude, longitude)
            # Clip city, state, and country if necessary
            city = city[:32]
            state = state[:32]
            country = country[:32]
            
            return Response({'city': city, 'state': state, 'country': country})
        
        except:
            return Response(status=400)
