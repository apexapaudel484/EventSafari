from django.urls import path
from . import views

urlpatterns = [
    path('event', views.event, name='event'),
    path('create_event', views.create_event, name='create_event'),
]