from django.urls import path, include, re_path
from app2.views import RegistrationView_func, empty_view
from app2.email_verification import activate_email, send_verification_email
from app2.passwordverification import send_password_reset_email
from .adapter import GoogleLogin
from dj_rest_auth.urls import LoginView, LogoutView, UserDetailsView, PasswordChangeView, get_refresh_view, TokenVerifyView

urlpatterns = [
    
    path('auth/signup/', RegistrationView_func, name='account_signup'), #login + signp urls
    path('auth/password/reset/<username>/<useremail>/', send_password_reset_email, name='rest_password_reset'),
    path('auth/login/', LoginView.as_view(), name='rest_login'), #login needs email confirmation
    
    # URLs that require a user to be logged in with a valid session / token.
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('auth/user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('auth/password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    
    path('auth/activate_email/<uidb64>/<token>/', activate_email, name='activate_email'),
    path('auth/send_verification_email/<int:user_pk>/', send_verification_email, name='send_verification_email'), #send and verify user email and activate account urls
    
    path('auth/google/', GoogleLogin.as_view()), #google login
    
    path('auth/account_inactive/', empty_view, name='account_inactive'), #reverse path to not crash with is_active=false
    
]