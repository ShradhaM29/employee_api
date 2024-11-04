from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_email(self, value):
        email = value.strip().lower()  # Normalize email to lower case and trim whitespace
        # Allow existing email if updating the same record
        if self.instance and self.instance.email.lower() == email:
            return value
        # Check for case-insensitive uniqueness
        if Employee.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_name(self, value):
        if not value.strip():  # Ensure name is not empty or whitespace
            raise serializers.ValidationError("Name cannot be empty.")
        if len(value) > 50:  # Example maximum length for name
            raise serializers.ValidationError("Name cannot exceed 50 characters.")
        return value
