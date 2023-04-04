from django.urls import path

from .views import RenderHomePageView

app_name = "customers"


urlpatterns = [
    path('', RenderHomePageView.as_view(), name='home_page'),
]
