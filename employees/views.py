from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        # Handle bulk creation if request data is a list
        is_bulk = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_bulk)

        # Validate data and raise exception if invalid
        serializer.is_valid(raise_exception=True)

        # Save data and return the response
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_object(self):
        try:
            # Use built-in method to handle object retrieval or raise 404
            return super().get_object()
        except Employee.DoesNotExist:
            raise Http404("Employee not found")


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'role']
