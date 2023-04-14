from rest_framework import serializers
from .models import Event


class event_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'summary', 'description', 'url', 'start', 'end', 'created', 'changed', 'status', 'online_event',
                'hide_start_date', 'hide_end_date', 'free', 'waitlist', 'view_counter', 'owner', 'category',
                'age_restriction', 'language', 'timezone', 'video_url', 'published', 'fully_booked', 'organizer']
        
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
