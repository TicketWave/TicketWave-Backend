from django.urls import path
from .views import event_Create, event_Destroy, event_List, event_Update, event_Retrieve, event_private_Retrieve, \
    event_increment_view_counter, follow_event, event_follower_count, event_count_query, event_unpublish, event_publish, event_copy, event_price, \
        event_amount_tickets_sold, event_sales_total_and_sales_by_ticket, event_tags


urlpatterns = [

    path('list/', event_List.as_view()),
    path('retrieve/<pk>/', event_Retrieve.as_view()),


    path('create/', event_Create.as_view()),
    path('destroy/<pk>/', event_Destroy.as_view()),
    path('update/<pk>/', event_Update.as_view()),
    path('private/retrieve/<pk>/', event_private_Retrieve.as_view()),

    path('increment_view_counter/<pk>/', event_increment_view_counter.as_view()),
    path('follow_event/<event_id>/', follow_event.as_view()),
    path('add_tag/<event_id>/<tag_id>/', event_tags.as_view()),
    path('event_follower_count/<event_id>/', event_follower_count.as_view()),

    path('event_count_query/', event_count_query.as_view()),
    path('unpublish/<event_id>/', event_unpublish.as_view()),
    path('publish/<event_id>/', event_publish.as_view()),
    path('copy/<event_id>/', event_copy.as_view()),
    path('price/<event_id>/', event_price.as_view()),
    path('total_sales/<event_id>/', event_sales_total_and_sales_by_ticket.as_view()),
    path('sales_by_ticket/<event_id>/', event_sales_total_and_sales_by_ticket.as_view()),
    path('amount_of_tickets_sold/<event_id>/', event_amount_tickets_sold.as_view()),
]
