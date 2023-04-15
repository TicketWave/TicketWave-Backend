from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .Serializers import UsersSerializer
from .models import Users
from rest_framework.response import Response

class UserById(APIView):
   queryset = Users.objects.all()
   def get_user(request, user_id=None, email=None):
       if user_id is not None:
           user = Users.objects.filter(id=user_id).values('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login','is_public','image_id')
       elif email is not None:
           user = Users.objects.filter(email=email).values('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login','is_public','image_id')
       else:
           return Response({'error': 'Please specify a user ID or email'})
       if user.exists():
           return Response({'user': user[0]})
       else:
           return Response({'error': 'User not found'})
class UserProfile(APIView):
    queryset = Users.objects.all()
    def get(self, request):
        user = request.user
        user = Users.objects.filter(id=pk).values('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login','is_public','image_id')
        serializer = UsersSerializer(user)
        return Response(serializer.data)
