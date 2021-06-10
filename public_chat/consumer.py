import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer


#AsyncWebsocketconsumer gets the username
class ChatRoomConsumer(AsyncJsonWebsocketConsumer):
    #using asyncronous function
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        #creating a new group that utilizes chat room consumer
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        #accept is needed to allow WS connections
        

    async def disconnect(self, close_code):
        '''
        disconnecting group from websocket
        '''
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    #need to receive text_data from input field from user first 
    #so that we can send it to the group
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,  
            {
                'type': 'chatroom_message',
                'message': message, 
                'username':username,

            }     

        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username':username,
        }))