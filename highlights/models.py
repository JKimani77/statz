from django.db import models
from cloudinary.models import CloudinaryField
#import datetime as dt
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField



class Apidata(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()
    image = CloudinaryField('image')
    competition_name = models.CharField(max_length=30)

    def save_apidata(self):
        self.save()
    def def_apidata(self):
        self.delete()

    @classmethod
    def get_apidata_id(cls,id):
        apidata = cls.objects.filter(id = id).all()
        return apidata
    
class Peopletoo(models.Model):
    folowers = models.IntegerField(default=0)

    def __str__(self):
        return self.pk

class People(models.Model):
    folowing = models.IntegerField(default=0)

    def __str__(self):
        return self.pk

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'usermodel', default=2)
    profile_pic = CloudinaryField('image')
    followers = models.ForeignKey(Peopletoo, on_delete=models.CASCADE )
    following = models.ForeignKey(People, on_delete=models.CASCADE)

    def save_profile(self):
        self.save()
    def del_profile(self):
        self.delete()

    @classmethod
    def get_profile_id(cls,user):
        profile = cls.objects.filter(id=user.id).all()
        return profile

    def update_profile(self,bio):
        self.bio = bio
        self.save()



class Comments(models.Model):
    whenposted = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=100)
    profileid = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def save_comment(self):
        self.save()
    def del_comment(self):
        self.delete()
#Football=title, url, image, competition_name
#Profile-user(onetoone),profilepic,bio,followers,following
#Others=following,followed
#comments-comment,profile_id(foreign)