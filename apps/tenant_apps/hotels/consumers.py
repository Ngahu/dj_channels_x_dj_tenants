from channels.consumer import AsyncConsumer, StopConsumer
from django.db import connection

# from channels.generic.websocket import AsyncWebsocketConsumer


class ChatHotelConsumer(AsyncConsumer):

    async def websocket_connect(self, message):
        current_user = self.scope['user']

        currrent_tenant = self.scope['tenant'] #request.tenant
        
        print(current_user, "websocket_connect current_user")
        print(message, "websocket_connect message")

        print(currrent_tenant, "currrent_tenant")

        print(connection.schema_name, "connection.schema_name")

        await self.send({"type": "websocket.accept"})



    async def websocket_receive(self, message):
        """
        Called when a WebSocket frame is received. Decodes it and passes it
        to receive().
        """
        if "text" in message:
            await self.receive(text_data=message["text"])
        else:
            await self.receive(bytes_data=message["bytes"])

    async def receive(self, text_data=None, bytes_data=None):
        """
        Called with a decoded WebSocket frame.
        """
        if text_data:
            print("received text_data", text_data)
        
        elif bytes_data:
            print("bytes_data received", bytes_data)


    async def websocket_disconnect(self, message):

        print("websocket_disconnect", message)
        raise StopConsumer()
