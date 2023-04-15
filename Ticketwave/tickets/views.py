from django.http import Http404
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tickets.models import Ticket
from tickets.serlializers import TicketSerializer


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
    

class TicketList(APIView):
    """
    List all Tickets, or create a new Ticket
    """
  
    def get(self, request, format=None):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer( tickets, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data) 
        if serializer.is_valid(): # after data is received from request, serializer changes it into object
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketDetail(APIView):
    """
    Retrieve, update or delete a ticket instance
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
