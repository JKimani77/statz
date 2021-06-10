from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers, viewsets, routers
from .models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic','followers', 'following')


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apidata
        fields = ('title','url','image','competition_name')

