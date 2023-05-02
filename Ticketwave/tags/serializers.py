from rest_framework import serializers
from .models import Tags


class tags_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
