from django.contrib import admin
from django.urls import path, include
from login.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('cadastro/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('', include('validade.urls')),
    ]
