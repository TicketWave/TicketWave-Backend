from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.hashers import make_password
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from dj_rest_auth.serializers import JWTSerializer
from rest_framework.response import Response

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        try:
            user = super().save_user(request, user, form, commit)
            
            data = form.cleaned_data
            user.is_public = data.get('is_public')
            user.image_id = data.get('image_id')

            user.is_active = False
            user.save()
        except:
            pass
        return user

    def set_password(self, user, password):
        return super().set_password(user, make_password(password))


class GoogleLogin(SocialLoginView):  # if you want to use Implicit Grant, use this
    adapter_class = GoogleOAuth2Adapter
    serializer_class = JWTSerializer

    def post(self, request):
        try:
            # Parse the response from the provider
            self.request.POST = self.request.POST.copy()
            self.request.POST['access_token'] = request.data['access_token']
            self.request.POST['code'] = ''
            return super(GoogleLogin, self).post(request)
        except OAuth2Error as e:
            # Handle errors
            return Response({'detail': str(e)})

# for front end, login happens from this url template and redirect it to /auth/google
# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=<CALLBACK_URL_YOU_SET_ON_GOOGLE>&prompt=consent&response_type=token&client_id=<YOUR CLIENT ID>&scope=openid%20email%20profile

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    serializer_class = JWTSerializer

    def post(self, request):
        try:
            # Parse the response from the provider
            self.request.POST = self.request.POST.copy()
            self.request.POST['access_token'] = request.data['access_token']
            self.request.POST['code'] = ''
            return super(FacebookLogin, self).post(request)
        except OAuth2Error as e:
            # Handle errors
            return Response({'detail': str(e)})
