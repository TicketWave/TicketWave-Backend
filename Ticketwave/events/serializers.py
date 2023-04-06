from rest_framework import serializers
from .models import Event


        
class event_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['listed', 'shareable', 'invite_only', 'show_remaining', 'password', 'capacity', 'capacity_is_custom', 'followers']
        
class event_private_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
class IncrementViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'view_counter']
