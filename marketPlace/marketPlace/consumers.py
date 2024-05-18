import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync
from conversation.models import Conversation, ConversationMessage
from django.contrib.auth.models import User
from datetime import datetime

class inboxConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        query_string = self.scope['query_string'].decode('utf-8')  # Decode the query string from bytes to string
        user_value = query_string.split('=')[1]  # Split the query string based on '=' and get the second part (value)

        self.room_group_name = user_value
        print("User:", user_value)


        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        # print("request : ", self.scope)

        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected',
        }))


    def receive(self, text_data):
        
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
        conversation_id = text_data_json['conversation_id']
        user = text_data_json['user']

        conversation = Conversation.objects.get(id=conversation_id)

        members = conversation.members.all()
        other_user = members.exclude(username=user).first()


        async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
        {
            'type': 'chat_message',
            'message':message,
            "conversation_id": conversation_id,
            "user" : user,
            "reciever" : 'no'
        })
        print(other_user)

        async_to_sync(self.channel_layer.group_send)(
            f"{other_user}",
            {
                'type': 'chat_message',
                'message':message,
                "conversation_id": conversation_id,
                "user" : user,
                "reciever" : 'yes'
            }
        )

    def chat_message(self, event):
        message = event['message']
        conversation_id = event['conversation_id']
        username = event['user']
        reciever = event['reciever']

        if reciever == 'no':
            if message and conversation_id and username:
                try:
                    conversation = Conversation.objects.get(id=conversation_id)
                    user = User.objects.get(username=username)

                except (Conversation.DoesNotExist, User.DoesNotExist):
                    return
                
                conversation_message = ConversationMessage.objects.create(
                    conversation=conversation,
                    content=message,
                    created_by=user
                )
                conversation_message.save()

        current_time = datetime.now().strftime("%B %d, %Y, %I:%M %p").lower()


        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'reciever': reciever,
            'created_by' : f"{username}",
            "created_at" : current_time,
        }))



    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )



    def emitmessage(self ,data):
        text_data_json = json.loads(data)
        print("emit: ", text_data_json)
