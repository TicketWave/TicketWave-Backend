from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
	path('create/', views.add_ticket_classes, name='add-ticket-classes'),
	path('get/', views.view_ticket_classes, name='view-ticket-classes'),
	path('update/<int:pk>/', views.update_tickets_classes, name='update-ticket-classes'),

]