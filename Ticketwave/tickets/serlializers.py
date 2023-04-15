from django.db.models import fields
from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = (
			'name',
			'event',
			'user',
			'price',
			'SalesStart',
			'StartTime',
			'SalesEnd',
			'EndTime',
			'CodeName',
			'RevealHidden',
			'Discount',
			'PromoStart',
			'PromoEnds',
			'ApplyCode',
			'TicketLimit',
			#'CSVfile',
			'amount',
			'State',
			'Capacity'
		)
		


# serializes data in model to be viewed in state of json in api










