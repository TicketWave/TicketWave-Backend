from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import AttendeeSerializer
from .models import Attendees
from users.models import Users
from events.models import Event
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics

class createAttendee(generics.CreateAPIView):
    serializer_class = AttendeeSerializer
    queryset = Attendees.objects.all()

class manageAttendees(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttendeeSerializer
    queryset = Attendees.objects.all()