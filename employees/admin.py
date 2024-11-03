from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'role', 'date_joined')  # Customize columns as needed
    search_fields = ('name', 'email', 'department', 'role')  # Optional: Add search fields
    list_filter = ('department', 'role')  # Optional: Add filters

admin.site.register(Employee, EmployeeAdmin)
