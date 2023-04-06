from .views import order_Create, order_Destroy, order_List, order_Retrieve, order_Update, order_count_by_event
from django.urls import path


urlpatterns = [

    path('list/', order_List.as_view()),
    path('retrieve/<pk>/', order_Retrieve.as_view()),
    path('create/', order_Create.as_view()),
    path('destroy/<pk>/', order_Destroy.as_view()),
    path('update/<pk>/', order_Update.as_view()),

    path('retrieve_event_order_count/<int:event>/',
         order_count_by_event.as_view()),  # test this
]
