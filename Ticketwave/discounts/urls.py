from . import views
from django.urls import path

urlpatterns = [
    path('', views.manageDiscounts),
    path('<int:id>', views.addDelUpDiscount)
]
