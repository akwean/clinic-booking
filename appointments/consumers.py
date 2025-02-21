import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AppointmentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("appointments", self.channel_name)
        if self.scope["user"].is_authenticated:
            await self.channel_layer.group_add(f"appointment_{self.scope['user'].id}", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("appointments", self.channel_name)
        if self.scope["user"].is_authenticated:
            await self.channel_layer.group_discard(f"appointment_{self.scope['user'].id}", self.channel_name)

    async def appointment_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))

    async def appointment_status_update(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))
