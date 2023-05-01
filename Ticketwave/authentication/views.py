from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import redirect
from urllib.parse import urlencode
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Error, OAuth2Client
from decouple import config


class RegistrationView(RegisterView):
    serializer_class = CustomRegisterSerializer


RegistrationView_func = RegistrationView.as_view()


def empty_view():
    return Response()


class GoogleConnect(SocialLoginView):
    client_class = OAuth2Client
    adapter_class = GoogleOAuth2Adapter
    
    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('google_callback'))
    
def google_callback(request):
    params = urlencode(request.GET)
    #print(params)
    frontend_google_login = config('frontend_google_login') #'http://localhost:3000/google/' #
    return redirect(f'{frontend_google_login}{params}')

class FacebookConnect(SocialLoginView):
    client_class = OAuth2Client
    adapter_class = FacebookOAuth2Adapter
    
    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('facebook_callback'))
    
def facebook_callback(request):
    params = urlencode(request.GET)
    #print(params)
    frontend_facebook_login = config('frontend_facebook_login') #'http://localhost:3000/facebook/' #
    return redirect(f'{frontend_facebook_login}{params}')