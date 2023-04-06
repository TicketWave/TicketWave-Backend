from .models import Event
from .serializers import event_Serializer, event_private_Serializer, IncrementViewSerializer
from .filters import eventFilter
from .pagination import StandardResultsSetPagination
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from authentication.permissions import Is_eventowner_or_readonly, Is_eventowner
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class event_List(ListAPIView): 
    queryset = Event.objects.all()
    
    serializer_class = event_Serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = StandardResultsSetPagination 
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = eventFilter
    search_fields = ['^name'] 
    ordering_fields = ['name', 'start', 'end',  'created', 'changed', 'view_counter']
    
    def get_queryset(self):
        
        queryset = Event.objects.all()
        
        try:
            online_event = self.request.query_params.get('online_event', None)
            if online_event is not None:
                if online_event.lower() == 'true': queryset = queryset.filter(online_event__in=[True])
                elif online_event.lower() == 'false': queryset = queryset.filter(online_event__in=[False])
                
            hide_start_date = self.request.query_params.get('hide_start_date', None)
            if hide_start_date is not None:
                if hide_start_date.lower() == 'true': queryset = queryset.filter(hide_start_date__in=[True])
                elif hide_start_date.lower() == 'false': queryset = queryset.filter(hide_start_date__in=[False])
                
            hide_end_date = self.request.query_params.get('hide_end_date', None)
            if hide_end_date is not None:
                if hide_end_date.lower() == 'true': queryset = queryset.filter(hide_end_date__in=[True])
                elif hide_end_date.lower() == 'false': queryset = queryset.filter(hide_end_date__in=[False])
            
            free = self.request.query_params.get('free', None)
            if free is not None:
                if free.lower() == 'true': queryset = queryset.filter(free__in=[True])
                elif free.lower() == 'false': queryset = queryset.filter(free__in=[False])
                
            listed = self.request.query_params.get('listed', None)
            if listed is not None:
                if listed.lower() == 'true': queryset = queryset.filter(listed__in=[True])
                elif listed.lower() == 'false': queryset = queryset.filter(listed__in=[False])
                
            waitlist = self.request.query_params.get('waitlist', None)
            if waitlist is not None:
                if waitlist.lower() == 'true': queryset = queryset.filter(waitlist__in=[True])
                elif waitlist.lower() == 'false': queryset = queryset.filter(waitlist__in=[False])
                
        except:
            #pass
            print("error happened while grabbing query params for event_List view")
            
        return queryset

class event_increment_view_counter(UpdateAPIView):
    serializer_class = IncrementViewSerializer
    queryset = Event.objects.all()
    #permission_classes = [AllowAny] #???
    
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_counter += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)   
    
class follow_event(APIView):
    #permission_classes = [IsAuthenticated]
    
    def post(self, request, event_id):
        user = request.user
        if not user.is_authenticated:
            return Response(status=401)
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response(status=404)

        event.followers.add(user)
        return Response(status=200)

    def delete(self, request, event_id):
        user = request.user
        if not user.is_authenticated:
            return Response(status=401)
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response(status=404)

        event.followers.remove(user)
        return Response(status=200)
    
class event_follower_count(APIView):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response(status=404)
        
        follower_count = event.followers.count()
        return Response({'follower_count': follower_count})

class event_Retrieve(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = event_Serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class event_Update(UpdateAPIView):
    queryset = Event.objects.all()
    lookup_field = 'pk'
    serializer_class = event_private_Serializer
    #permission_classes = [IsAuthenticated, Is_eventowner_or_readonly] #[AllowAny]#
    
    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class event_Destroy(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = event_private_Serializer
    #permission_classes = [IsAuthenticated, Is_eventowner_or_readonly]

class event_Create(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = event_private_Serializer
    #permission_classes = [IsAuthenticated] 

class event_private_Retrieve(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = event_private_Serializer
    #permission_classes = [IsAuthenticated, Is_eventowner]
