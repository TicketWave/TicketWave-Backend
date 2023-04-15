from . import views
from django.urls import path
from .views import UserProfile, UserAPI

urlpatterns = [
    path('<int:pk>/', UserAPI.as_view()),
    path('<str:email>/', UserAPI.as_view()),
    path('me/', UserProfile.as_view()),
]
