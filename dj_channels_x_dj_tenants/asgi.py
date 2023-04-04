"""
ASGI config for dj_channels_x_dj_tenants project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from apps.tenant_apps.hotels.routing import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from dj_channels_x_dj_tenants.middleware.main import AsyncTenantMainMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_channels_x_dj_tenants.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            AsyncTenantMainMiddleware(
                URLRouter(websocket_urlpatterns)
            )
        )
    )
})
