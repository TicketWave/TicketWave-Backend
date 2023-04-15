from django.urls import path
from .views import createAttendee, manageAttendees

urlpatterns = [
    path('<int:pk>/', manageAttendees.as_view()),
    # path('user/<int:user_id>/', ),
    path('create', createAttendee.as_view()),
    path('update/<int:pk>/', manageAttendees.as_view()),
    path('delete/<int:pk>/', manageAttendees.as_view()),   
]
