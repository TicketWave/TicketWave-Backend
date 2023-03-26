from django.urls import path
from .views import add_ticket_classes, update_tickets_classes, view_ticket_classes
from . import views

urlpatterns = [
	path('create/', add_ticket_classes.as_view()),
	path('get/', view_ticket_classes.as_view()),
	path('update/<int:pk>/', update_tickets_classes.as_view()),

]