from django.urls import path
from tickets.views import TicketList,TicketDetail


urlpatterns = [
path('', TicketList.as_view()),
path('<str:model>/<int:pk>/', TicketList.as_view()),
path('id/<int:pk>/', TicketDetail.as_view()),
]

#localhost/tickets