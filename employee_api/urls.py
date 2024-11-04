from django.contrib import admin  # Ensure this import is included
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from employees.views import home, EmployeeViewSet  # Import the EmployeeViewSet

from rest_framework.routers import DefaultRouter  # Import the router for viewsets

# Create a router and register the EmployeeViewSet
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),  # Ensure 'admin' is imported above
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh
    path('api/', include(router.urls)),  # Include the router URLs for employee CRUD operations
]
