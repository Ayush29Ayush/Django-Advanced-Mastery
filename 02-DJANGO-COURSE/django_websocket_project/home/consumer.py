from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class MainConsumer(WebsocketConsumer):

    def connect(self, **kwargs):
        self.room_name = "main_room"
        self.group_name = "main_room"
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.accept()
        self.send(text_data=json.dumps({"message": "connection made"}))

    def receive(self, text_data=None):
        print("Type: ", type(text_data), "Data: ", text_data)

    def disconnect(self, close_code):
        print("disconnected", close_code)


# import json
# from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = ("chat_room")  # You can set this dynamically based on user or URL

#         self.room_group_name = f"chat_{self.room_name}"

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "chat_message", "message": message}
#         )

#     async def chat_message(self, event):
#         message = event["message"]

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": message}))
