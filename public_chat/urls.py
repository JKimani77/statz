from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('<str:room_name>', views.room, name = 'room'),
]