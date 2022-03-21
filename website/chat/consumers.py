import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """ Asynchronous consumer which adds a channel to a group (group is defined by the room name in url parameters),
        receives a message and broadcasts it to all channels in the group, closes WebSocket connection. """
    async def connect(self):
        """ Accepts WebSocket connection and join the group. """
        self.room_name = self.scope['url_route']['kwargs']['room_name']         # get room name from url
        self.room_group_name = 'chat_%s' % self.room_name                       # convert room name to group name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        """ Removes channel from the group """
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """ Receives message from WebSocket. """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',                                         # specify method to be called on receive
                'message': message,
            }
        )

    async def chat_message(self, event):
        """ Receive message from room group. """
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': self.scope['user'].username,
        }))
