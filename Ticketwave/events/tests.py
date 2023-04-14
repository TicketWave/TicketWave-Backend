from django.test import TestCase
from .models import Event
from users.models import Users
from categories.models import Categories
from venues.models import Venue
from .serializers import event_Serializer, IncrementViewSerializer, event_private_Serializer
import datetime

# Create your tests here.
class EventTestCase(TestCase):
    
    def setUp(self):
        # Create instances of the related models
        user = Users.objects.create(username='testuser')
        category = Categories.objects.create(name='testcategory')
        venue = Venue.objects.create(name='testvenue')

        # Create an instance of Event to use in the tests
        self.event = Event.objects.create(
            name='Test Event',
            summary='Test summary',
            description='Test description',
            url='https://example.com',
            online_event=True,
            hide_start_date=False,
            hide_end_date=False,
            free=True,
            waitlist=False,
            status = 'draft',
            view_counter=0,
            age_restriction=False,
            fully_booked=False,
            published=False,
            organizer='Test Organizer',
            video_url='https://example.com/video',
            timezone='UTC',
            language='en',
            listed=True,
            shareable=True,
            invite_only=False,
            show_remaining=False,
            capacity=50,
            capacity_is_custom=False,
            start=datetime.datetime.now(),
            end=datetime.datetime.now() + datetime.timedelta(hours=1),
            owner=user,
            category=category,
            venue=venue
        )
        # Check that the serialized data is correct
        self.event_private_expected_data = {
            'id': self.event.id,
            'name': 'Test Event',
            'summary': 'Test summary',
            'description': 'Test description',
            'url': 'https://example.com',
            'start': self.event.start.isoformat(),
            'end': self.event.end.isoformat(),
            'created': self.event.created.isoformat(),
            'changed': self.event.changed.isoformat(),
            'status': 'draft',
            'online_event': True,
            'hide_start_date': False,
            'hide_end_date': False,
            'free': True,
            'waitlist': False,
            'view_counter': 0,
            'age_restriction': False,
            'fully_booked': False,
            'published': False,
            'organizer': 'Test Organizer',
            'video_url': 'https://example.com/video',
            'timezone': 'UTC',
            'language': 'en',
            'owner': self.event.owner.id,
            'category': self.event.category.id,
            'followers': [],
            'venue': self.event.venue.id,
            'listed': True,
            'shareable': True,
            'invite_only': False,
            'show_remaining': False,
            'capacity': 50,
            'capacity_is_custom': False
        }
        
        self.event_expected_data = {
            'name': 'Test Event',
            'summary': 'Test summary',
            'description': 'Test description',
            'url': 'https://example.com',
            'start': self.event.start.isoformat(),
            'end': self.event.end.isoformat(),
            'created': self.event.created.isoformat(),
            'changed': self.event.changed.isoformat(),
            'status': 'draft',
            'online_event': True,
            'hide_start_date': False,
            'hide_end_date': False,
            'free': True,
            'waitlist': False,
            'view_counter': 0,
            'age_restriction': False,
            'fully_booked': False,
            'published': False,
            'organizer': 'Test Organizer',
            'video_url': 'https://example.com/video',
            'timezone': 'UTC',
            'language': 'en',
            'owner': self.event.owner.id,
            'category': self.event.category.id,
        }
        
        self.view_counter_expected_data = {
            'id': 1,
            'view_counter': 0
        }
        
    def Test_Event_Model(self):
        self.assertEqual(self.event.name, "Test Event")
        self.assertEqual(self.event.listed, True)
        # test database record is created successfully
    
    def test_serializer(self):
        # Serialize the MyModel instance
        serializer = event_Serializer(self.event)
        # Check that the serialized data is correct
        self.assertEqual(serializer.data, self.expected_data)
        
    def Test_event_Serizalizer(self):
        # Serialize the MyModel instance
        serializer = event_Serializer(self.event)
        # Check that the serialized data is correct
        self.assertEqual(serializer.data, self.event_expected_data)
        
    def Test_event_private_Serizalizer(self):
        # Serialize the Event instance
        serializer = event_private_Serializer(self.event)
        # Check that the serialized data is correct
        self.assertEqual(serializer.data, self.event_private_expected_data)
    
    def Test_IncrementView_Serizalizer(self):
        # Serialize the Event instance
        serializer = IncrementViewSerializer(self.event)
        # Check that the serialized data is correct
        self.assertEqual(serializer.data, self.view_counter_expected_data)
            
    def Test_increment_viewers(self):
        #serializer.save and serizalizer.valid
        self.assertEqual(self.event.view_counter, 0)
        self.event.view_counter += 1
        self.event.save()
        self.assertEqual(self.event.view_counter, 1)
        
    def Test_event_get_follower_count(self):   
        follower_count = self.event.followers.count()
        self.assertEqual(follower_count, 0)
        
    def Test_event_follow(self):
        followtestuser = Users.objects.create(username='followtestuser')
        self.event.followers.add(followtestuser)
        follower_count = self.event.followers.count()
        self.assertEqual(follower_count, 1)
        
    def Test_event_unfollow(self):   
        followtestuser = Users.objects.get(username='followtestuser')
        self.event.followers.remove(followtestuser)
        follower_count = self.event.followers.count()
        self.assertEqual(follower_count, 0)
    
    def Test_event_publish(self):
        serializer = event_Serializer(self.event, data={
                    'status': 'live',
                    'publish': True,
                    'start': self.event.end.isoformat(),
                    'end': self.event.start.isoformat(),
                    'password': 'lol',
                }, partial=True)
        if serializer.is_valid():
            serializer.save()
    
    def Test_event_unpublish(self):
        serializer = event_Serializer(self.event, data={
                    'status': 'canceled',
                    'publish': False,
                    }, partial=True)
        if serializer.is_valid():
            serializer.save()
        
    def Test_event_update(self):
        self.assertEqual(self.event.invite_only, False)
        self.event.invite_only = True
        self.event.save()
        self.assertEqual(self.event.invite_only, True)

    def Test_event_copy(self):
        self.assertEqual(self.event.pk, 1)
        self.event.pk = None
        self.event.save()
        self.assertNotEqual(self.event.pk, 1)
        
    def Test_event_destroy(self):
        event = Event.objects.get(id=1)
        self.assertEqual(event.pk, 1)
        event.delete()
        try:
            event = Event.objects.get(id=1)
        except Event.DoesNotExist:
            self.assertEqual(1, 1, "Event with id 1 does not exist")