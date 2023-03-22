from rest_framework import serializers
from .models import Media


        
class media_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
        
