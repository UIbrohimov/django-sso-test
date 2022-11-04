from django.contrib import admin
from django.urls import path, include

from simple_sso.sso_server.server import Server
from user.views import login_view, logout_view, register

server = Server()


urlpatterns = [
    path('sso/', include(server.get_urls())),
    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('register/', register, name="register"),
    path('user/', include('user.urls', namespace='user'))
]
