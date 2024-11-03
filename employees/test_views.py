from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee


class EmployeeTests(APITestCase):

    def test_create_employee(self):
        url = reverse('employee-list')  # Assuming your router is set up correctly
        data = {
            "name": "Emily Clark",
            "email": "emily.clark@example.com",
            "department": "Finance",
            "role": "Analyst"
        }
        response = self.client.post(url, data, format='json')

        # Assert that the employee was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)

        # Verify that the employee's details are correct
        employee = Employee.objects.get(email="emily.clark@example.com")
        self.assertEqual(employee.name, "Emily Clark")
        self.assertEqual(employee.department, "Finance")
        self.assertEqual(employee.role, "Analyst")
        self.assertIsNotNone(employee.date_joined)  # Check that date_joined is auto-generated

    def test_get_employee_detail(self):
        # Create an employee to test retrieval
        employee = Employee.objects.create(name="David Grey", email="david.grey@example.com", department="Engineering",
                                           role="Developer")
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.get(url)

        # Assert that the employee details are returned correctly
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "David Grey")  # Corrected from "John Doe" to "David Grey"

    def test_delete_employee(self):
        # Create an employee to test deletion
        employee = Employee.objects.create(name="John Doe", email="john.doe@example.com", department="Engineering",
                                           role="Developer")
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.delete(url)

        # Assert that the employee was deleted successfully
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)  # Verify that the employee no longer exists
