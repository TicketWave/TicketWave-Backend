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
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('venues/', include('venues.urls')),
    path('tickets/', include('tickets.urls')),
    path('categories/', include('categories.urls')),
    path('discounts/', include('discounts.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('pricing/', include('pricing.urls')),
    path('tickets/', include('tickets.urls')),
    path('attendees/', include('attendees.urls')),
    path('', include('authentication.urls')),
]
