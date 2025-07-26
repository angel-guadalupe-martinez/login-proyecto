from django.urls import path
from .views import login_view

urlpatterns = [
    path('login/', login_view),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginapp.urls')),
]
