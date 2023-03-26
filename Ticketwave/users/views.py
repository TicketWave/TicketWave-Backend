from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UsersSerializer
from .models import Users
from rest_framework.response import Response

class UserById(APIView):
   queryset = Users.objects.all()
   def get(self, request, id):
       user = Users.objects.get(pk=id)
       serializer = UsersSerializer(user)
       return Response(serializer.data)
class UserProfile(APIView):
    queryset = Users.objects.all()
    def get(self, request):
        user = request.user
        serializer = UsersSerializer(user)
        return Response(serializer.data)
