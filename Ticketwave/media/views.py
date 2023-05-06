from django.shortcuts import render
from .models import Media
from .serializers import media_Serializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

class manageMedia(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= media_Serializer
    queryset = Media.objects.all()
    lookup_field= 'id'
 
 class createMedia(generics.CreateAPIView):
    serializer_class= media_Serializer
    queryset= Media.objects.all()
    
    
@api_view(('GET',))
def listMediaByEvent(request,event_id):
    media= Media.objects.filter(event_id = event_id)
    serializer= media_Serializer(media, many= True)
    return Response(serializer.data)
