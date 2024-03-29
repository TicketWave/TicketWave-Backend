"""Ticketwave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/events/", include("events.urls")),
    path("api/venues/", include("venues.urls")),
    path("api/tickets/", include("tickets.urls")),
    path("api/categories/", include("categories.urls")),
    path("api/discounts/", include("discounts.urls")),
    path("api/users/", include("users.urls")),
    path("api/orders/", include("orders.urls")),
    path("api/attendees/", include("attendees.urls")),
    path("api/tags/", include("tags.urls")),
    path("api/media/", include("media.urls")),
    path("", include("authentication.urls")),
]
