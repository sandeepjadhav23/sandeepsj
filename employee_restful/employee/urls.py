from django.urls import path

from employee import views

urlpatterns = [
    path('employees/', views.EmployeeListCreate.as_view()),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDelete.as_view()),
]
