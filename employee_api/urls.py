# employee_Api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),  # This includes the URLs from the employees app
]
