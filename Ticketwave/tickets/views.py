from django.http import Http404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from tickets.models import Ticket
from tickets.serlializers import TicketSerializer
   

class TicketList(GenericAPIView):
    """
    List all Tickets, or create a new Ticket
    """

    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
  
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
