from django.urls import path, re_path

from .consumers import ChatHotelConsumer

websocket_urlpatterns = [

    re_path("", ChatHotelConsumer.as_asgi()),
]


