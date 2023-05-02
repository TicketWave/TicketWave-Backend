from django.db import models
from users.models import Users
from categories.models import Categories
from venues.models import Venue
from django.core.validators import MinValueValidator

# Create your models here.


class Event(models.Model):
    
    status_choices = [
        ('draft', 'draft'),
        ('live', 'live'),
        ('started', 'started'),
        ('ended', 'ended'),
        ('completed', 'completed'),
        ('canceled', 'canceled'),
    ]
    
    name = models.CharField(max_length=80)
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    start = models.DateTimeField()  # "2004-03-15 12:01" format value example
    end = models.DateTimeField()
    # changes automatically as added
    created = models.DateTimeField(auto_now_add=True)
    # changes automatically as saved
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16, default='draft', choices=status_choices)
    online_event = models.BooleanField()
    hide_start_date = models.BooleanField()
    hide_end_date = models.BooleanField()
    free = models.BooleanField(default=False)
    waitlist = models.BooleanField(default=False)
    view_counter = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    age_restriction = models.BooleanField(default=False)
    
    fully_booked = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    organizer = models.CharField(max_length=80)
    video_url = models.URLField(blank=True)
    timezone = models.CharField(max_length=10)
    language = models.CharField(max_length=20)

    owner = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=1, related_name='event')
    category = models.ForeignKey(
        Categories, on_delete=models.SET_DEFAULT, default=1, related_name='event')

    followers = models.ManyToManyField(Users, related_name='following_event')
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='event')

    # private fields will limit access to by serializer

    listed = models.BooleanField(default=True)
    shareable = models.BooleanField(default=True)
    invite_only = models.BooleanField(default=False)
    show_remaining = models.BooleanField(default=False)
    password = models.TextField(null=True)
    capacity = models.IntegerField(default=50)
    capacity_is_custom = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
