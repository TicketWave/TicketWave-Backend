from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.createMedia.as_view()),
    path('<int:pk>/', views.manageMedia.as_view()),
    path('event/<int:event_id>/', views.listMediaByEvent)
]
