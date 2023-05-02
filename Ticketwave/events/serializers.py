from rest_framework import serializers
from .models import Event


class event_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'summary', 'description', 'url', 'start', 'end', 'created', 'changed', 'status', 'online_event',
                'hide_start_date', 'hide_end_date', 'free', 'waitlist', 'view_counter', 'owner', 'category',
                'age_restriction', 'language', 'timezone', 'video_url', 'published', 'fully_booked', 'organizer', 'to_be_announced',
                'recurring_end_day', "recurring_start_day", 'recurring_end_month', "recurring_start_month", 'recurring', 'recurring_frequency']
        
        #exclude = ['listed', 'shareable', 'invite_only', 'show_remaining',
        #        'password', 'capacity', 'capacity_is_custom', 'followers']


class event_private_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class IncrementViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'view_counter']
