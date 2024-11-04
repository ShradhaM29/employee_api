from django.contrib import admin  # Make sure this import is included
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from employees.views import home, EmployeeList, EmployeeDetail

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),  # Ensure 'admin' is imported above
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh
    path('api/employees/', EmployeeList.as_view(), name='employee-list'),  # List and create employees
    path('api/employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),  # Retrieve, update, delete employee
]
