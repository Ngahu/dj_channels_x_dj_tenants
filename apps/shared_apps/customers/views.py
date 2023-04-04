from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView



class RenderHomePageView(TemplateView):
    template_name = "home.html"