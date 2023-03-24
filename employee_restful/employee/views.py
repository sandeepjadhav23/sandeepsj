from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from employee.pagination import MyPagination
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    pagination_class=MyPagination

class EmployeeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer