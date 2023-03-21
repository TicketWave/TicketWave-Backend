from rest_framework import serializers
from .models import Discounts

class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = ['id', 'code', 'type', 'start_date', 'end_date', 'percent_off', 'quantity_available', 'quantity_sold', 'event_id']