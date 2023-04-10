from .models import Venue
from .serializers import venue_Serializer
from .filters import venueFilter
from .pagination import StandardResultsSetPagination
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


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
    #permission_classes = [IsAuthenticated, Is_eventowner_or_readonly]
    
    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class venue_Destroy(DestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = venue_Serializer
    #permission_classes = [IsAuthenticated, Is_eventowner_or_readonly]

class venue_Create(CreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = venue_Serializer
    #permission_classes = [IsAuthenticated] 
