"""
proyecto ejemplo neunapp - django permissions
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls')),
    path('', include('applications.nota.urls')),
]
