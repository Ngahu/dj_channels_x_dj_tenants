
from apps.shared_apps.customers.models import Client, Domain
from channels.db import database_sync_to_async
from django.conf import settings
from django.db import connection
from django.urls import set_urlconf


class AsyncTenantMainMiddleware:
    """
    This middleware should be placed at the very top of the middleware stack.
    Selects the proper database schema using the request host. Can fail in
    various ways which is better than corrupting or revealing data.
    """

    def __init__(self, app):
        # Store the ASGI application we were passed
        self.app = app
    
    @database_sync_to_async
    def get_tenant(self, domain_model, hostname):
        domain = domain_model.objects.select_related('tenant').get(domain=hostname)
        return domain.tenant

    async def __call__(self, scope, receive, send):
        connection.set_schema_to_public()

        try:
            hostname = await self.hostname_from_request(scope)
        except Exception:
            from django.http import HttpResponseNotFound
            return HttpResponseNotFound()
        
        domain_model = Domain

        try:
            tenant = await self.get_tenant(domain_model, hostname)
        
        except domain_model.DoesNotExist:
            raise Exception(f"No tenant for hostname {hostname}")
        except Exception:
            raise Exception(f"No tenant for hostname {hostname}")
        
        tenant.domain_url = hostname
        scope['tenant'] = tenant
        connection.set_tenant(tenant)

        return await self.app(scope, receive, send)

    async def hostname_from_request(self, scope):
        headers_dict = scope
        headers = dict(headers_dict['headers'])
        host = headers.get(b'host', b'').decode().split(':')[0]
        return host
