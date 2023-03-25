from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UsersSerializer
from .models import Users

def home(request):
    return JsonResponse({'message': 'This is a test response.'})
class UserById(APIView):
   def get(self, request, id):
       user = User.objects.get(pk=id)
       serializer = UsersSerializer(user)
       return Response(serializer.data)
class UserProfile(APIView):
    def get(self, request):
        user = request.user
        serializer = UsersSerializer(user)
        return Response(serializer.data)
