import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from django_app import models


class ChatConsumer(AsyncWebsocketConsumer):
    @sync_to_async  # соединение асинхронного кода и синхронного
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = models.Room.objects.get(slug=room)

        # сохранение сообщения в базу
        models.Message.objects.create(user=user, room=room, content=str(message))

    async def connect(self):
        # определение имение комнаты
        # {'url_route': {'kwargs': {'room_name': ...}...}...}
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]

        # определение канала(группы)
        self.room_group_name = f'chat_online_{self.room_name}'

        # добавления пользователя в группы
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        # удаление пользователя из группы
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data: bytes):
        # от фронтенда приходит в формате байтов JSON-строка
        # chatSocket.send(JSON.stringify({
        #             'message': message,
        #             'username': userName,
        #             'room': roomName
        #         }));

        data = json.loads(text_data)  # bytes(JSON) -> dict

        # извлечение полученных данных
        username = data["username"]
        room = data["room"]
        message = data["message"]

        # сохраняет сообщения в БД
        await self.save_message(username, room, message)

        # "рассылка" сообщения всем подписанным в группе
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",  # async def chat_message(self, event)
                # 'type': "notification",
                "message": message,
                "username": username,
                "room": room,
            }
        )

    async def chat_message(self, event):  # 'type': "chat_message",
        message = event["message"]
        username = event["username"]
        room = event["room"]

        await self.send(text_data=json.dumps({  # dict -> str(JSON)
            "message": message,
            "username": username,
            "room": room,
        }))
