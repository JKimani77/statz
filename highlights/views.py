import requests
from django.http  import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import PermissionManager, User
from django.contrib.auth import login,logout,authenticate
from requests.api import get

from .models import *
from .serializers import *
from .requests import *


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status



def home(request):
    data=requests.get('https://free-football-soccer-videos.p.rapidapi.com/?rapidapi-key=6c61f61a64mshb7f6dd3b49823b4p1ea082jsnbd55b4b7071b').json()
    return render(request, 'a.html' ,{"data":data})

def login(request):
    if request.method=='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username,password=password)
            
            if user.is_active:
                login(request,user)
                return redirect(home)
            else:
                return "Your account is inactive"
    else:
        form = LoginForm()
    return render(request, 'registration/login.html',{"form":form})

def logout_user(request):
    logout(request)
    return redirect(home)
#


def login():
    pass
def logout_user():
    pass
def search_by_title():
    pass
def comment():
    pass
def profile():
    pass
def view_profile():
    pass


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes((permissions.AllowAny,))
class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


@permission_classes((permissions.AllowAny,))
class ApiList(APIView):
    def get (self, request, format = None):
        all_data = Apidata.objects.all()
        serializers = ApiSerializer(all_data, many=True)
        return Response(serializers.data)

    def post(self, request, format = None):
        serializers = ApiSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.status.HTTP_400_BAD_REQUEST)
        
   