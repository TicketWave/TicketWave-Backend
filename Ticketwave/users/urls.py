from django.urls import path
from users.views import UserProfile, UserAPIByEmail, UserAPIByID

urlpatterns = [
    path('id/<int:id>/', UserAPIByID.as_view()),
    path('email/<str:email>/', UserAPIByEmail.as_view()),
    path('me/', UserProfile.as_view()),
]
