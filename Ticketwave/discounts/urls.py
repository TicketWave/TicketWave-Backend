from . import views
from django.urls import path

urlpatterns = [
    path("create/", views.createDiscount.as_view()),
    path("<int:pk>/", views.manageDiscounts.as_view()),
    path("event/<int:event_id>/", views.listDiscountsByEvent),
    path("apply/<str:discount_code>", views.applyDiscount),
    path("check/<str:discount_code>", views.applyDiscount),
]
