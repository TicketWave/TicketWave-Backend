from django.urls import path, include, re_path
from .views import RegistrationView_func, empty_view
from .email_verification import activate_email, send_verification_email
from .passwordverification import send_password_reset_email
from .adapter import GoogleLogin, FacebookLogin
from dj_rest_auth.urls import LoginView, LogoutView, UserDetailsView, PasswordChangeView, get_refresh_view, TokenVerifyView

urlpatterns = [
    
    #login + signp urls
    path('auth/signup/', RegistrationView_func, name='account_signup'), 
    path('auth/password/reset/<username>/<useremail>/', send_password_reset_email, name='rest_password_reset'),
    path('auth/login/', LoginView.as_view(), name='rest_login'), #login needs email confirmation
    
    # URLs that require a user to be logged in with a valid session / token.
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('auth/password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    
    #send and verify user email and activate account urls
    path('auth/activate_email/<uidb64>/<token>/', activate_email, name='activate_email'),
    path('auth/send_verification_email/<int:user_pk>/', send_verification_email, name='send_verification_email'), 
    
    #social logins (google login and facebook login)
    path(r'auth/google/login/$', GoogleLogin.as_view(),name='google_login'), 
    path(r'auth/facebook/login/$', FacebookLogin.as_view(), name='facebook_login'),
    path(r'^accounts/', include('allauth.urls')),
    
    #reverse path to not crash with is_active=false
    path('auth/account_inactive/', empty_view, name='account_inactive'), 
    
]