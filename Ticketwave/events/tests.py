from django.test import TestCase
from .models import Event
from users.models import Users
from categories.models import Categories
from venues.models import Venue
from .serializers import event_Serializer, IncrementViewSerializer, event_private_Serializer
import datetime

#to run
#python manage.py test events.tests

# Create your tests here.
class EventTestCase(TestCase):
    
    def setUp(self):
        # Create instances of the related models
        user = Users.objects.create(username='testuser', email='jlennon@beatles.com', password='glasssssss')
        category = Categories.objects.create(name='testcategory', short_name='testcat')
        venue = Venue.objects.create(name='testvenue', longitude=53.480837, latitude=53.480837)

        # Create an instance of Event to use in the tests
        self.event = Event.objects.create(
            id = 1,
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
            start= datetime.datetime(2004,3,14,12,1), # "2004-03-15 12:01",
            end=datetime.datetime(2005,3,14,12,1), #"2005-03-15 12:01",
            changed = datetime.datetime(2004,3,14,12,1),
            created = datetime.datetime(2004,3,14,12,1),
            owner=user,
            category=category,
            venue=venue
        )
        event1 = Event.objects.get(name = "Test Event")
        self.test_event_pk = event1.pk
        
        # Check that the serialized data is correct
        self.event_private_expected_data = {
            'id': self.test_event_pk,
            'name': 'Test Event',
            'summary': 'Test summary',
            'description': 'Test description',
            'url': 'https://example.com',
            'start': '2004-03-14T12:01:00Z',
            'end': '2005-03-14T12:01:00Z',
            'created': '2004-03-14T12:01:00Z',
            'changed': '2004-03-14T12:01:00Z',
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
            'owner': self.event.owner.pk,
            'category': self.event.category.pk,
            'followers': [],
            'venue': self.event.venue.pk,
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
            'start': '2004-03-14T12:01:00Z',
            'end': '2005-03-14T12:01:00Z',
            'created': '2004-03-14T12:01:00Z',
            'changed': '2004-03-14T12:01:00Z',
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
            'owner': self.event.owner.pk,
            'category': self.event.category.pk,
        }
        
        self.view_counter_expected_data = {
            'id': 1,
            'view_counter': 0
        }
        
    def test_Event_Model(self):
        event1 = Event.objects.get(name = "Test Event")
        self.assertEqual(event1.name, "Test Event")
        self.assertEqual(event1.listed, True)
        # test database record is created successfully
        
    def test_event_Serizalizer(self):
        # Serialize the MyModel instance
        event1 = Event.objects.get(name = "Test Event")
        serializer = event_Serializer(event1)
        # Check that the serialized data is correct
        self.assertTrue(serializer.is_valid())
        
    def test_event_private_Serizalizer(self):
        # Serialize the Event instance
        event1 = Event.objects.get(name = "Test Event")
        serializer = event_private_Serializer(event1)
        # Check that the serialized data is correct
        self.assertTrue(serializer.is_valid())
    
    def test_IncrementView_Serizalizer(self):
        # Serialize the Event instance
        event1 = Event.objects.get(name = "Test Event")
        serializer = IncrementViewSerializer(event1)
        # Check that the serialized data is correct
        self.assertEqual(serializer.data, self.view_counter_expected_data)
            
    def test_increment_viewers(self):
        event1 = Event.objects.get(name = "Test Event")
        self.assertEqual(event1.view_counter, 0)
        event1.view_counter += 1
        event1.save()
        self.assertEqual(event1.view_counter, 1)
        
    def test_event_get_follower_count(self):   
        event1 = Event.objects.get(name = "Test Event")
        follower_count = event1.followers.count()
        self.assertEqual(follower_count, 0)
        
    def test_event_follow(self):
        event1 = Event.objects.get(name = "Test Event")
        followtestuser = Users.objects.create(username='followtestuser', email='followtestuser@beatles.com', password='gasyhdias')
        event1.followers.add(followtestuser)
        follower_count = event1.followers.count()
        self.assertEqual(follower_count, 1)
        
    def test_event_unfollow(self):   
        event1 = Event.objects.get(name = "Test Event")
        followtestuser = Users.objects.create(username='followtestuser2', email='followtestuse22r@beatles.com', password='ga2syhdias')
        event1.followers.add(followtestuser)
        follower_count = event1.followers.count()
        self.assertEqual(follower_count, 1)
        event1.followers.remove(followtestuser)
        follower_count = event1.followers.count()
        self.assertEqual(follower_count, 0)
    
    def test_event_publish(self):
        event1 = Event.objects.get(name = "Test Event")
        serializer = event_Serializer(event1, data={
                    'status': 'live',
                    'publish': True,
                    'start': self.event.end,
                    'end': self.event.start,
                    'password': 'lol',
                }, partial=True)
        self.assertTrue(serializer.is_valid())
    
    def test_event_unpublish(self):
        event1 = Event.objects.get(name = "Test Event")
        serializer = event_Serializer(event1, data={
                    'status': 'canceled',
                    'publish': False,
                    }, partial=True)
        self.assertTrue(serializer.is_valid())
        
    def test_event_update(self):
        event1 = Event.objects.get(name = "Test Event")
        self.assertEqual(event1.invite_only, False)
        event1.invite_only = True
        event1.save()
        self.assertEqual(event1.invite_only, True)

    def test_event_copy(self):
        event1 = Event.objects.get(name = "Test Event")
        self.assertEqual(event1.pk, self.test_event_pk)
        event1.pk = None
        event1.name = 'copied'
        event1.save()
        self.assertNotEqual(event1.pk, self.test_event_pk)
        