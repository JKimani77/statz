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
from .forms import *

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


def createprofile(request):
    currentuser = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = currentuser
            profile.save_profile()
            return redirect(home)
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html',{"form":form})
    

def viewprofile(request, id):
    profile = Profile.objects.filter(user = id).all()
    return render(request, 'profile_view.html',{"profile":profile}) 

def search_by_title():
    pass
def comment():
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

 