from . import views
from django.urls import path

urlpatterns = [
    path('', views.listCategories),
    path('<int:category_id>/', views.listSubcategoriesByCategory)
]
