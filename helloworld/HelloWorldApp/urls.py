from django.contrib import admin
from django.urls import path, include
from .views import sayHello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sayHello, name='sayHello')
]
