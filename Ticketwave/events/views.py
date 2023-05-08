from .models import Event
from orders.models import Order
from tickets.models import Ticket
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
    search_fields = ['name']
    ordering_fields = ['name', 'start', 'end',
                       'created', 'changed', 'view_counter']

    def get_queryset(self):

        queryset = Event.objects.all()

        try:
            online_event = self.request.query_params.get('online_event', None)
            if online_event is not None:
                if online_event.lower() == 'true':
                    queryset = queryset.filter(online_event__in=[True])
                elif online_event.lower() == 'false':
                    queryset = queryset.filter(online_event__in=[False])

            hide_start_date = self.request.query_params.get(
                'hide_start_date', None)
            if hide_start_date is not None:
                if hide_start_date.lower() == 'true':
                    queryset = queryset.filter(hide_start_date__in=[True])
                elif hide_start_date.lower() == 'false':
                    queryset = queryset.filter(hide_start_date__in=[False])

            hide_end_date = self.request.query_params.get(
                'hide_end_date', None)
            if hide_end_date is not None:
                if hide_end_date.lower() == 'true':
                    queryset = queryset.filter(hide_end_date__in=[True])
                elif hide_end_date.lower() == 'false':
                    queryset = queryset.filter(hide_end_date__in=[False])

            free = self.request.query_params.get('free', None)
            if free is not None:
                if free.lower() == 'true':
                    queryset = queryset.filter(free__in=[True])
                elif free.lower() == 'false':
                    queryset = queryset.filter(free__in=[False])

            listed = self.request.query_params.get('listed', None)
            if listed is not None:
                if listed.lower() == 'true':
                    queryset = queryset.filter(listed__in=[True])
                elif listed.lower() == 'false':
                    queryset = queryset.filter(listed__in=[False])

            waitlist = self.request.query_params.get('waitlist', None)
            if waitlist is not None:
                if waitlist.lower() == 'true':
                    queryset = queryset.filter(waitlist__in=[True])
                elif waitlist.lower() == 'false':
                    queryset = queryset.filter(waitlist__in=[False])

            age_restriction = self.request.query_params.get(
                'age_restriction', None)
            if age_restriction is not None:
                if age_restriction.lower() == 'true':
                    queryset = queryset.filter(age_restriction__in=[True])
                elif age_restriction.lower() == 'false':
                    queryset = queryset.filter(age_restriction__in=[False])
                    
            fully_booked = self.request.query_params.get(
                'fully_booked', None)
            if fully_booked is not None:
                if fully_booked.lower() == 'true':
                    queryset = queryset.filter(fully_booked__in=[True])
                elif fully_booked.lower() == 'false':
                    queryset = queryset.filter(fully_booked__in=[False])
                    
            published = self.request.query_params.get(
                'published', None)
            if published is not None:
                if published.lower() == 'true':
                    queryset = queryset.filter(published__in=[True])
                elif published.lower() == 'false':
                    queryset = queryset.filter(published__in=[False])
            
            invite_only = self.request.query_params.get(
                'invite_only', None)
            if invite_only is not None:
                if invite_only.lower() == 'true':
                    queryset = queryset.filter(invite_only__in=[True])
                elif invite_only.lower() == 'false':
                    queryset = queryset.filter(invite_only__in=[False])
            
            to_be_announced = self.request.query_params.get(
                'to_be_announced', None)
            if to_be_announced is not None:
                if to_be_announced.lower() == 'true':
                    queryset = queryset.filter(to_be_announced__in=[True])
                elif to_be_announced.lower() == 'false':
                    queryset = queryset.filter(to_be_announced__in=[False])
            
            recurring = self.request.query_params.get(
                'recurring', None)
            if recurring is not None:
                if recurring.lower() == 'true':
                    queryset = queryset.filter(recurring__in=[True])
                elif recurring.lower() == 'false':
                    queryset = queryset.filter(recurring__in=[False])

        except:
            # pass
            print("error happened while grabbing query params for event_List view")

        return queryset


class event_count_query(ListAPIView):
    queryset = Event.objects.all()

    serializer_class = event_Serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = eventFilter
    search_fields = ['^name']

    def get_queryset(self):

        queryset = Event.objects.all()

        try:
            online_event = self.request.query_params.get('online_event', None)
            if online_event is not None:
                if online_event.lower() == 'true':
                    queryset = queryset.filter(online_event__in=[True])
                elif online_event.lower() == 'false':
                    queryset = queryset.filter(online_event__in=[False])

            hide_start_date = self.request.query_params.get(
                'hide_start_date', None)
            if hide_start_date is not None:
                if hide_start_date.lower() == 'true':
                    queryset = queryset.filter(hide_start_date__in=[True])
                elif hide_start_date.lower() == 'false':
                    queryset = queryset.filter(hide_start_date__in=[False])

            hide_end_date = self.request.query_params.get(
                'hide_end_date', None)
            if hide_end_date is not None:
                if hide_end_date.lower() == 'true':
                    queryset = queryset.filter(hide_end_date__in=[True])
                elif hide_end_date.lower() == 'false':
                    queryset = queryset.filter(hide_end_date__in=[False])

            free = self.request.query_params.get('free', None)
            if free is not None:
                if free.lower() == 'true':
                    queryset = queryset.filter(free__in=[True])
                elif free.lower() == 'false':
                    queryset = queryset.filter(free__in=[False])

            listed = self.request.query_params.get('listed', None)
            if listed is not None:
                if listed.lower() == 'true':
                    queryset = queryset.filter(listed__in=[True])
                elif listed.lower() == 'false':
                    queryset = queryset.filter(listed__in=[False])

            waitlist = self.request.query_params.get('waitlist', None)
            if waitlist is not None:
                if waitlist.lower() == 'true':
                    queryset = queryset.filter(waitlist__in=[True])
                elif waitlist.lower() == 'false':
                    queryset = queryset.filter(waitlist__in=[False])

            age_restriction = self.request.query_params.get(
                'age_restriction', None)
            if age_restriction is not None:
                if age_restriction.lower() == 'true':
                    queryset = queryset.filter(age_restriction__in=[True])
                elif age_restriction.lower() == 'false':
                    queryset = queryset.filter(age_restriction__in=[False])
            
            fully_booked = self.request.query_params.get(
                'fully_booked', None)
            if fully_booked is not None:
                if fully_booked.lower() == 'true':
                    queryset = queryset.filter(fully_booked__in=[True])
                elif fully_booked.lower() == 'false':
                    queryset = queryset.filter(fully_booked__in=[False])
                    
            published = self.request.query_params.get(
                'published', None)
            if published is not None:
                if published.lower() == 'true':
                    queryset = queryset.filter(published__in=[True])
                elif published.lower() == 'false':
                    queryset = queryset.filter(published__in=[False])
            
            invite_only = self.request.query_params.get(
                'invite_only', None)
            if invite_only is not None:
                if invite_only.lower() == 'true':
                    queryset = queryset.filter(invite_only__in=[True])
                elif invite_only.lower() == 'false':
                    queryset = queryset.filter(invite_only__in=[False])
                    
            to_be_announced = self.request.query_params.get(
                'to_be_announced', None)
            if to_be_announced is not None:
                if to_be_announced.lower() == 'true':
                    queryset = queryset.filter(to_be_announced__in=[True])
                elif to_be_announced.lower() == 'false':
                    queryset = queryset.filter(to_be_announced__in=[False])
            
            recurring = self.request.query_params.get(
                'recurring', None)
            if recurring is not None:
                if recurring.lower() == 'true':
                    queryset = queryset.filter(recurring__in=[True])
                elif recurring.lower() == 'false':
                    queryset = queryset.filter(recurring__in=[False])

        except:
            # pass
            print("error happened while grabbing query params for event_List view")

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()

        return Response({'count': count}, status=200)


class event_increment_view_counter(UpdateAPIView):
    serializer_class = IncrementViewSerializer
    queryset = Event.objects.all()
    permission_classes = [AllowAny] 

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_counter += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class event_sales_total(APIView):
    def get(self, request, event_id, *args, **kwargs):
        try:
            total = 0
            Tickets = Ticket.objects.filter(event=event_id)
            for ticket in Tickets:
                total += ticket.price * ticket.amount
            return Response(status=200, data={"total sales": total})
        except:
            return Response(status=400)
        
class sales_by_ticket(APIView):
    def get(self, request, event_id, *args, **kwargs):
        try:
            sales = {}
            amount = {}
            Tickets = Ticket.objects.filter(event=event_id)
            for ticket in Tickets:
                amount[ticket.type] = amount.get(ticket.type, 0) + ticket.amount
                sales[ticket.type] = sales.get(ticket.type, 0) + ticket.price * ticket.amount
            return Response(status=200, data={"sales": sales, "amount": amount})
        except:
            return Response(status=400)
        
class event_amount_tickets_sold(APIView):
    def get(self, request, event_id, *args, **kwargs):
        try:
            total = 0
            Tickets = Ticket.objects.filter(event=event_id)
            for ticket in Tickets:
                total += ticket.amount
            return Response(status=200, data={"tickets sold": total})
        except:
            return Response(status=400)


class follow_event(APIView):
    permission_classes = [IsAuthenticated]

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
    
class event_tags(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id, tag_id):
        user = request.user
        if not user.is_authenticated:
            return Response(status=401)
        try:
            event = Event.objects.get(id=event_id)
            tag = Event.objects.get(id=tag_id)
        except:
            return Response(status=404)
        event.tags.add(tag)
        return Response(status=200)

    def delete(self, request, event_id, tag_id):
        user = request.user
        if not user.is_authenticated:
            return Response(status=401)
        try:
            event = Event.objects.get(id=event_id)
            tag = Event.objects.get(id=tag_id)
        except:
            return Response(status=404)
        event.tags.remove(tag)
        return Response(status=200)


class event_follower_count(APIView):
    permission_classes = [AllowAny]
    def get(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response(status=404)

        follower_count = event.followers.count()
        return Response({'follower_count': follower_count})
    
class event_price(APIView):
    permission_classes = [AllowAny]
    def get(self, request, event_id):
        try:
            ticket = Ticket.objects.filter(event=event_id).first()
        except Ticket.DoesNotExist:
            return Response(status=404)

        return Response({'price': ticket.price})

def check_order_status(event):
    orders = Order.objects.filter(event=event)
    for order in orders:
        if order.status == 'pending' or order.status == 'completed':
            return False
    return True

def check_publish_requirements(event):
    try:
        if event.name == '' and event.description == '': 
                return False
        if len(Ticket.objects.filter(event=event)) == 0: return False
        #check for valid payment option too, required, done, not implmemented in this project
        return True
    except:
        return False

class event_unpublish(APIView):
    permission_classes = [IsAuthenticated, Is_eventowner]
    def get(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            result = check_order_status(event)
            if result :
                serializer = event_Serializer(event, data={
                    'status': 'canceled',
                    'publish': False,
                    }, partial=True)
                if serializer.is_valid():
                    serializer.save()
                return Response({'unpublished': True}, status=200)
            else: return Response({'unpublished': False}, status=400)
        except:
            return Response(status=400)
        
class event_publish(APIView):
    permission_classes = [IsAuthenticated, Is_eventowner]
    def get(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            result = check_publish_requirements(event)
            start = self.request.data.get('start', None)
            end = self.request.data.get('end', None)
            password = self.request.data.get('password', None)
            if result and start != None and password != None:
                serializer = event_Serializer(event, data={
                    'status': 'live',
                    'publish': True,
                    'start': start,
                    'password': password,
                }, partial=True)
                if serializer.is_valid():
                    serializer.save()
                return Response({'published': True}, status=200)
            else: return Response({'published': False}, status=400)
        except:
            return Response(status=400)
        
class event_copy(APIView):
    permission_classes = [IsAuthenticated, Is_eventowner]
    def get(self, request, event_id):
        try:
            try:
                original_event = Event.objects.get(id=event_id)
                # event.pk = None
                # event.save()
                event = Event.objects.create(
            name=original_event.name,
            type = original_event.type,
            summary=original_event.summary,
            description=original_event.description,
            url=original_event.url,
            online_event=original_event.online_event,
            hide_start_date=original_event.hide_start_date,
            hide_end_date=original_event.hide_end_date,
            free=original_event.free,
            waitlist=original_event.waitlist,
            status = original_event.status,
            view_counter=0,
            age_restriction=original_event.age_restriction,
            fully_booked=original_event.fully_booked,
            published=original_event.published,
            organizer=original_event.organizer,
            video_url=original_event.video_url,
            timezone=original_event.timezone,
            language=original_event.language,
            listed=original_event.listed,
            shareable=original_event.shareable,
            invite_only=original_event.invite_only,
            show_remaining=original_event.show_remaining,
            capacity=original_event.capacity,
            capacity_is_custom=original_event.capacity_is_custom,
            start=original_event.start, #datetime.datetime(2004,3,14,12,1),  #"2004-03-15 12:01",
            end=original_event.end,#datetime.datetime(2005,3,14,12,1), #"2005-03-15 12:01",
            
            owner=original_event.owner,
            category=original_event.category,
            sub_category=original_event.sub_category,
            venue=original_event.venue
            
        )
                return Response({'copy': True}, status=200)
            except:
                return Response({'copy': False}, status=400)
        except:
            return Response(status=400)
    
class event_Retrieve(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = event_Serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class event_Update(UpdateAPIView):
    queryset = Event.objects.all()
    lookup_field = 'pk'
    serializer_class = event_private_Serializer
    permission_classes = [IsAuthenticated, Is_eventowner_or_readonly]

    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class event_Destroy(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = event_private_Serializer
    permission_classes = [IsAuthenticated, Is_eventowner_or_readonly]


class event_Create(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = event_private_Serializer
    permission_classes = [IsAuthenticated]


class event_private_Retrieve(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = event_private_Serializer
    permission_classes = [IsAuthenticated, Is_eventowner]
