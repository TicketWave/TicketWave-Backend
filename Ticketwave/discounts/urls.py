from . import views
from .views import ManageDiscounts
from django.urls import path

urlpatterns = [
    path('', ManageDiscounts.as_view()),
    # path('<int:id>', views.addDelUpDiscount)
]
