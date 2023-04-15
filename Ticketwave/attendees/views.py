from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .Serializers import AttendeeSerializer
from .models import Attendee
from users.models import Users
from events.models import Event
from rest_framework import status
from rest_framework.decorators import api_view

class ManageAttendee(APIView):
  def get_attendee_by_id(request,attendee_id):
    attendee=Attendee.objects.get(id=attendee_id)
    serializer=AttendeeSerializer(attendee)
    return Response(serializer.data)
  def get_attendee_by_event(request,event_id):
    attendees= Attendee.objetcs.filter(event_id=event_id)
    serializer=AttendeeSerializer(attendees,many =True)
    return Response(serializer.data, safe=False)
  def get_attendee_by_user(request,user_id):
    attendees=Attendee.objects.filter(user_id=user_id)
    serializer=AttendeeSerializer(attendees,many=True)
    return Response(serializer.data,safe=False)
   
    
  @api_view(['POST'])
  def create_attendee(request):
    seliazer=AttendeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  @api_view(['PUT'])
  def update_attendee(request,pk):
    attendee=Attendee.objects.get(pk=attendee_id)
    serializer=AttendeeSerializer(attendee,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  @api_view(['DELETE'])
  def delete_attendee(request,pk):
    attendee=Attendee.objects.get(pk=attendee_id)
    attendee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
