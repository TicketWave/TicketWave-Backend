from django.urls import path
from .views import RegistrationView_func, empty_view
from .email_verification import activate_email, send_verification_email
from .passwordverification import send_password_reset_email
from .views import GoogleConnect, google_callback, FacebookConnect, facebook_callback
from dj_rest_auth.urls import LoginView, LogoutView, PasswordChangeView, get_refresh_view, TokenVerifyView
from allauth.socialaccount.providers.google import views as googleviewlogin #form is handled in front end just for testing here

urlpatterns = [
    
    #login + signp urls
    path('api/auth/signup/', RegistrationView_func, name='account_signup'), 
    path('api/auth/password/reset/<username>/<useremail>/', send_password_reset_email, name='rest_password_reset'),
    path('api/auth/login/', LoginView.as_view(), name='rest_login'), #login needs email confirmation
    
    # URLsapi/ that require a user to be logged in with a valid session / token.
    path('api/auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/auth/password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    
    #send api/and verify user email and activate account urls
    path('api/auth/activate_email/<uidb64>/<token>/', activate_email, name='activate_email'),
    path('api/auth/send_verification_email/<int:user_pk>/', send_verification_email, name='send_verification_email'), 
    
    #sociaapi/l logins (google login and facebook login)
    path('api/google/login/connect/', GoogleConnect.as_view(), name = 'google_connect'),
    path('api/google/login/callback/', google_callback, name = 'google_callback'),
    path('api/google/login/login/', googleviewlogin.oauth2_login, name = 'googleviewlogin'), #form for testing login in backend should be done in front for real project
    
    path('api/facebook/login/connect/', FacebookConnect.as_view(), name = 'facebook_connect'),
    path('api/facebook/login/callback/', facebook_callback, name = 'facebook_callback'),
    
    #reverapi/se path to not crash with is_active=false
    path('api/auth/account_inactive/', empty_view, name='account_inactive'), 
    
]