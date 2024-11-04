from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee


class EmployeeTests(APITestCase):

    def setUp(self):
        # Create an employee for use in multiple tests
        self.employee_data = {
            "name": "David Grey",
            "email": "david.grey@example.com",
            "department": "Engineering",
            "role": "Developer"
        }
        self.employee = Employee.objects.create(**self.employee_data)

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
        self.assertEqual(Employee.objects.count(), 2)  # Check that the employee count has increased

        # Verify that the employee's details are correct
        employee = Employee.objects.get(email="emily.clark@example.com")
        self.assertEqual(employee.name, "Emily Clark")
        self.assertEqual(employee.department, "Finance")
        self.assertEqual(employee.role, "Analyst")
        self.assertIsNotNone(employee.date_joined)  # Check that date_joined is auto-generated

    def test_create_employee_duplicate_email(self):
        url = reverse('employee-list')
        response = self.client.post(url, self.employee_data, format='json')

        # Assert that a duplicate email raises a validation error
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], "This email is already in use.")

    def test_get_employee_detail(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.get(url)

        # Assert that the employee details are returned correctly
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "David Grey")

    def test_get_employee_detail_not_found(self):
        url = reverse('employee-detail', args=[999])  # Non-existing employee ID
        response = self.client.get(url)

        # Assert that a 404 is returned for non-existing employee
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Employee not found")

    def test_delete_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.delete(url)

        # Assert that the employee was deleted successfully
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)  # Verify that the employee no longer exists

    def test_delete_employee_not_found(self):
        url = reverse('employee-detail', args=[999])  # Non-existing employee ID
        response = self.client.delete(url)

        # Assert that a 404 is returned for non-existing employee
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Employee not found")
