from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'role', 'date_joined')  # Display these columns
    search_fields = ('name', 'email', 'department', 'role')  # Enables search by these fields
    list_filter = ('department', 'role')  # Adds filter options for department and role

admin.site.register(Employee, EmployeeAdmin)
