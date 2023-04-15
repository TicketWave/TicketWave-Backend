from django.urls import path
from tickets.views import TicketList,TicketDetail


urlpatterns = [
path('', TicketList.as_view()),
path('id/<int:pk>/', TicketDetail.as_view()),
]