from . import views
from django.urls import path

urlpatterns = [
    path("create/", views.createMedia.as_view()),
    path("event/<int:event_id>/", views.manageMedia.as_view()),
    path("events/<int:event_id>/", views.listMediaByEvent),
]
