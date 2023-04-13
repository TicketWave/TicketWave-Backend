from django.urls import path
from .views import venue_Create, venue_Destroy, venue_List, venue_Update, venue_Retrieve, venue_get_location


urlpatterns = [
    
    path('list/', venue_List.as_view()),
    path('retrieve/<pk>/', venue_Retrieve.as_view()),
    path('create/', venue_Create.as_view()),
    path('destroy/<pk>/', venue_Destroy.as_view()),
    path('update/<pk>/', venue_Update.as_view()),
    path('user_location/', venue_get_location.as_view()),
]
