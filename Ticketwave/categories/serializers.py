from rest_framework import serializers
from .models import Categories

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'short_name', 'resource_uri', 'parent_category']