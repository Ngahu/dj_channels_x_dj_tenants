from django.urls import path

from .views import HotelsListView, TenantHomePageView

app_name = "hotels"


urlpatterns = [
    path('', TenantHomePageView.as_view(), name='tenant_home_page'),
    path('hotels/', HotelsListView.as_view(), name='hotels_home_page'),
]
