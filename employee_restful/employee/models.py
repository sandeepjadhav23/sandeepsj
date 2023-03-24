from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'),('F', 'Female'), ('T','Transgender')))
    department = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
