from rest_framework.response import Response

from dj_rest_auth.registration.views import RegisterView 
from .serializers import CustomRegisterSerializer



class RegistrationView(RegisterView):
    serializer_class = CustomRegisterSerializer
RegistrationView_func = RegistrationView.as_view()



def empty_view():
    return Response()