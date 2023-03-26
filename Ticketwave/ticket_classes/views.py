from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TicketClass
from .serlializers import TicketClassSerializer

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_ticket_classes': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)

class add_ticket_classes(APIView):
	queryset = TicketClass.objects.all()
	def post(request):
		ticket_class = TicketClassSerializer(data=request.data)
		if TicketClass.objects.filter(**request.data).exists():
				raise serializers.ValidationError('This data already exists')
		
		if ticket_class.is_valid():
			ticket_class.save()
			return Response(ticket_class.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
class update_tickets_classes(APIView):
	queryset = TicketClass.objects.all()
	def put(request, pk):
		queryset = TicketClass.objects.all()
		ticket_class = TicketClass.objects.get(pk=pk)
		data = TicketClassSerializer(instance=ticket_class, data=request.data)
	
		if data.is_valid():
			data.save()
			return Response(data.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)
	
class view_ticket_classes(APIView):
	queryset = TicketClass.objects.all()
	def get(request, *args, **kwargs):
		queryset = TicketClass.objects.all()
		# checking for the parameters from the URL
		try:
			ticket_classes = TicketClass.objects.all()
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		# if there is something in items else raise error
		if ticket_classes:
			serializer = TicketClassSerializer(ticket_classes, many=True)
			return Response(serializer.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)
    

# @api_view(['PUT'])
# def update_tickets_classes(request, pk):
#     queryset = TicketClass.objects.all()
#     ticket_class = TicketClass.objects.get(pk=pk)
#     data = TicketClassSerializer(instance=ticket_class, data=request.data)
 
#     if data.is_valid():
#         data.save()
#         return Response(data.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
# @api_view(['GET'])
# def view_ticket_classes(request):
	
# 	queryset = TicketClass.objects.all()
# 	# checking for the parameters from the URL
# 	if request.query_params:
# 		ticket_classes = TicketClass.objects.filter(**request.query_params.dict())
# 	else:
# 		ticket_classes = TicketClass.objects.all()

# 	# if there is something in items else raise error
# 	if ticket_classes:
# 		serializer = TicketClassSerializer(ticket_classes, many=True)
# 		return Response(serializer.data)
# 	else:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
