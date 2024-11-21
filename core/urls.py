
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')),
    path('', include('users.urls')),
    path("accounts/", include("allauth.urls")), 
]
