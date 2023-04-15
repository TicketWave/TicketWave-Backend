from . import views
from django.urls import path
from .views import UserById, UserProfile
urlpatterns = [
    path('<int:id>/', UserById.as_view()),
    path('<string:email>/', UserById.as_view()),
    path('me/', UserProfile.as_view()),
]
