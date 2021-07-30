from django.contrib import admin
from django.urls import path, include
from pollstask import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pollstask.urls')),
]
