from django.urls import path
from .views import add_tickets, update_tickets, view_tickets, TicketList


urlpatterns = [
path('tickets/', TicketList.as_view()),

]