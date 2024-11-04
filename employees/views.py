from django.http import HttpResponse, Http404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer

def home(request):
    """Home view that displays a welcome message."""
    return HttpResponse("""
        <h1>Welcome to the Employee Management API</h1>
        <p>This API allows you to manage employee records effectively.</p>
        <p>Visit the <a href="/admin/">Admin Site</a> to manage the application.</p>
        <p>For more information on using the API, please refer to the documentation in the README file.</p>
    """)

class EmployeeList(generics.ListCreateAPIView):
    """
    API view to handle listing all employees and creating a new employee.
    Supports bulk creation if the request data is a list.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        # Check if the request data is a list for bulk creation
        is_bulk = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_bulk)

        # Validate data and raise exception if invalid
        serializer.is_valid(raise_exception=True)

        # Save the new employee(s) and return the response
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a single employee.
    Returns a 404 error if the employee does not exist.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_object(self):
        """Retrieve the employee object or raise 404 if not found."""
        try:
            return super().get_object()
        except Employee.DoesNotExist:
            raise Http404("Employee not found")


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API view to handle CRUD operations for employees.
    Supports filtering by department and role.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'role']
