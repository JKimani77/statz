from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class PublicChatRoom(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False) 
    users = models.ManyToManyField(User, help_text="users connected to chat" )

    def __str__(self):
        return self.title


    def connect_user(self, user):
        '''
        return true if user is added to user list
        '''
        is_user_added = False
        if not user in self.users.all():
            self.users.add(user)
            self.save()
            is_user_added = True
        elif user in self.users.all():
            is_user_added = True
        return is_user_added

    def disconnect_user(self, user):
        '''
        return true if user is removed from users list
        '''
        is_user_removed = False
        if user in self.users.all():
            self.user.remove(user)
            self.save()
            is_user_added = True
        return is_user_removed

    @property
    def group_name(self):
        '''
        returns channel group name that sockets shld subscribe to and 
        get messages
        '''
        return f"PublicChatRoom-{self.id}"

class PublicRoomChatMessageManager(models.Manager):
    def by_room(self, room):
        '''
        retrieving new messages first by ordering by (-timestamp)
        '''
        qs = PublicRoomChatMessage.object.filter(room = room).order_by("-timestamp")
        return qs


class PublicRoomChatMessage(models.Model):
    '''
    chat model
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=False)

    objects = PublicRoomChatMessageManager()

    def __str__(self):
        return self.content

