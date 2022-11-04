from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from simple_sso.sso_client.client import Client

client = Client(
    server_url=settings.SIMPLE_SSO_SERVER,
    public_key=settings.SIMPLE_SSO_KEY,
    private_key=settings.SIMPLE_SSO_SECRET
)


from .views import some_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sso/', include(client.get_urls())),
    path('', some_view, name="verify")
]
