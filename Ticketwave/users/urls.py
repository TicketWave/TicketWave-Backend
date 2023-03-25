from . import views
from django.urls import path
from .views import UserById, UserProfile
urlpatterns = [
    path('users/<int:id>/', UserById.as_view()),
    path('user/', UserProfile.as_view()),
]
