from .views import tag_Create, tag_Destroy, tag_List, tag_Retrieve, tag_Update
from django.urls import path


urlpatterns = [

    path('list/', tag_List.as_view()),
    path('retrieve/<pk>/', tag_Retrieve.as_view()),
    path('create/', tag_Create.as_view()),
    path('destroy/<pk>/', tag_Destroy.as_view()),
    path('update/<pk>/', tag_Update.as_view()),

]
