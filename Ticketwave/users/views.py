from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth.models import User
from users.serializers import UsersSerializer
from rest_framework import status
from .models import Users
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field): # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class UserAPIByEmail(RetrieveUpdateDestroyAPIView):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer
   lookup_field = 'email'

class UserAPIByID(RetrieveUpdateDestroyAPIView):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer
   lookup_field = 'id'

class UserProfile(APIView):
    queryset = Users.objects.all()
    def get(self, request):
        user = request.user
        serializer = UsersSerializer(user)
        return Response(serializer.data)

