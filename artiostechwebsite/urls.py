
from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index),
    path('B50Gxe49/', admin.site.urls),
]
