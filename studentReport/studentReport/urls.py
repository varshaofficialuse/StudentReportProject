from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('studentApp/',include('studentApp.urls')),
    path('admin/', admin.site.urls),
]
