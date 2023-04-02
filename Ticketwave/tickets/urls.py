from django.urls import path
from .views import add_tickets, update_tickets, view_tickets
from . import views

urlpatterns = [
	path('create/', add_tickets.as_view()),
	path('get/', view_tickets.as_view()),
	path('update/<int:pk>/', update_tickets.as_view()),

]