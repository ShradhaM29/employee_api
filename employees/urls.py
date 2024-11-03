# employees/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'api/employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Optional
]

# Include the router URLs
urlpatterns += router.urls

