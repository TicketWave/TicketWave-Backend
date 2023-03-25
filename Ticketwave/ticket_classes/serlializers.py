from django.db.models import fields
from rest_framework import serializers
from .models import TicketClass

class TicketClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = TicketClass
		fields = ('category', 'subcategory', 'name', 'amount')