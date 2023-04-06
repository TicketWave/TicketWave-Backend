from django.urls import path
from .views import event_Create, event_Destroy, event_List, event_Update, event_Retrieve, event_private_Retrieve, \
    event_increment_view_counter, follow_event, event_follower_count


urlpatterns = [
    
    path('list/', event_List.as_view()),
    path('retrieve/<pk>/', event_Retrieve.as_view()),
    
    
    path('create/', event_Create.as_view()),
    path('destroy/<pk>/', event_Destroy.as_view()),
    path('update/<pk>/', event_Update.as_view()),
    path('private/retrieve/<pk>/', event_private_Retrieve.as_view()),
    
    path('increment_view_counter/<pk>/', event_increment_view_counter.as_view()),
    path('follow_event/<event_id>/', follow_event.as_view()),
    path('event_follower_count/<event_id>/', event_follower_count.as_view()),
]
