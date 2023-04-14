from rest_framework import serializers
from .models import Venue


class venue_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'
