from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat_%s' % self.room_name
		await self.channel_layer.group_add(
			self.room_name,
			self.room_group_name
		)
        await self.accept()
	async def disconnect(self):
		await self.channel_layer.group_discard(
			self.room_name,
			self.room_group_name
		)