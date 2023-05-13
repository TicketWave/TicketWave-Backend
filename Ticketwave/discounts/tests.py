from django.test import TestCase
from .models import Discounts
from events.models import Event
from users.models import Users
from categories.models import Categories
from venues.models import Venue
from .serializers import DiscountsSerializer
import datetime


class DiscountsTest(TestCase):
    def setUp(self):
        user = Users.objects.create(
            username="testuser", email="jlennon@beatles.com", password="glasssssss"
        )
        category = Categories.objects.create(name="testcategory", short_name="testcat")
        venue = Venue.objects.create(
            name="testvenue", longitude=53.480837, latitude=53.480837
        )

        event = Event.objects.create(
            id=1,
            name="Test Event",
            summary="Test summary",
            description="Test description",
            url="https://example.com",
            online_event=True,
            hide_start_date=False,
            hide_end_date=False,
            free=True,
            waitlist=False,
            status="draft",
            view_counter=0,
            age_restriction=False,
            fully_booked=False,
            published=False,
            organizer="Test Organizer",
            video_url="https://example.com/video",
            timezone="UTC",
            language="en",
            listed=True,
            shareable=True,
            invite_only=False,
            show_remaining=False,
            capacity=50,
            capacity_is_custom=False,
            start=datetime.datetime(2004, 3, 14, 12, 1),  # "2004-03-15 12:01",
            end=datetime.datetime(2005, 3, 14, 12, 1),  # "2005-03-15 12:01",
            changed=datetime.datetime(2004, 3, 14, 12, 1),
            created=datetime.datetime(2004, 3, 14, 12, 1),
            owner=user,
            category=category,
            venue=venue,
        )

        self.discount = Discounts.objects.create(
            code="test",
            type="test-type",
            end_date=datetime.datetime(2005, 3, 14, 12, 1),
            start_date=datetime.datetime(2004, 3, 14, 12, 1),
            percent_off=12,
            quantity_available=34,
            quantity_sold=16,
            event_id=event,
        )

        self.serializer = DiscountsSerializer(instance=self.discount)

    def test_Discounts_Model(self):
        discount1 = Discounts.objects.get(code="test")
        self.assertEqual(discount1.type, "test-type")
        self.assertEqual(discount1.percent_off, 12)

    def test_Discounts_Serializer(self):
        data = self.serializer.data
        self.assertEqual(data["code"], "test")
