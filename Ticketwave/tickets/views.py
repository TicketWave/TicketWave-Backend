from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ticket
from .serlializers import TicketSerializer

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_tickets': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)

class add_tickets(APIView):
	queryset = Ticket.objects.all()
	def post(request):
		ticket_class = TicketSerializer(data=request.data)
		if Ticket.objects.filter(**request.data).exists():
				raise serializers.ValidationError('This data already exists')
		
		if ticket_class.is_valid():
			ticket_class.save()
			return Response(ticket_class.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
class update_tickets(APIView):
	queryset = Ticket.objects.all()
	def put(request, pk):
		queryset = Ticket.objects.all()
		ticket_class = Ticket.objects.get(pk=pk)
		data = TicketSerializer(instance=ticket_class, data=request.data)
	
		if data.is_valid():
			data.save()
			return Response(data.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)
	
class view_tickets(APIView):
	queryset = Ticket.objects.all()
	def get(request, *args, **kwargs):
		queryset = Ticket.objects.all()
		# checking for the parameters from the URL
		try:
			tickets = Ticket.objects.all()
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		# if there is something in items else raise error
		if tickets:
			serializer = TicketSerializer(tickets, many=True)
			return Response(serializer.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)
    

