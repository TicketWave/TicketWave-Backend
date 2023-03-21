from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.hashers import make_password


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        try:
            user = super().save_user(request, user, form, commit)
            
            data = form.cleaned_data
            #user.is_public = data.get('is_public')

            user.is_active = False
            user.save()
        except:
            pass
        return user

    def set_password(self, user, password):
        return super().set_password(user, make_password(password))


class GoogleLogin(SocialLoginView):  # if you want to use Implicit Grant, use this
    adapter_class = GoogleOAuth2Adapter

# for front end get token from this url (token or code)  and post it to /auth/google
# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=<CALLBACK_URL_YOU_SET_ON_GOOGLE>&prompt=consent&response_type=token&client_id=<YOUR CLIENT ID>&scope=openid%20email%20profile
