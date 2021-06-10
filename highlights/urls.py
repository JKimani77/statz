from rest_framework.decorators import api_view
from highlights.views import UserViewSet, home
from django.urls import path, include
from rest_framework import serializers, viewsets, routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    #path('', include(router.urls)),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/data/', views.ApiList.as_view()),
    path('login/', views.login, name = 'login'),
    path('logout/',views.logout_user, name='logout'),
    
    
]