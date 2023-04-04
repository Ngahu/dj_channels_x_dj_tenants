from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.db import connection

class TenantHomePageView(TemplateView):
    template_name = "tenant_apps/tenant.html"



class HotelsListView(View):
    template_name = "tenant_apps/hotels-list.html"
    context = {}


    def get(self, request, *args, **kwargs):
        print(request.tenant, "Current tentnat")

        print(connection.schema_name, "connection.schema_name")

        return render(request, self.template_name, self.context)
