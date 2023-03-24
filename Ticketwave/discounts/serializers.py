from rest_framework import serializers
from .models import Discounts

class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = '__all__'