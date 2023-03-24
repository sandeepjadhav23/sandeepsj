# employee/serializers.py
from rest_framework import serializers
from employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'age', 'gender', 'department', 'salary']
        #fields = ['__all__']

    def validate_age(self, value):
        if value > 60:
            raise serializers.ValidationError("Age cannot be more than 60.")
        return value

    def validate_gender(self, value):
        if value not in ['M', 'F', 'T']:
            raise serializers.ValidationError("Gender should be 'M', 'F', or 'T'.")
        return value
