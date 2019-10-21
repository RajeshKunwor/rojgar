from django.urls import path
from .views import *

urlpatterns = [
    path('employee_dashboard', EmployeeDashboardView.as_view(), name='employee_dashboard'),
    path('register_employee', RegisterEmployeeView.as_view(), name='register_employee'),
    path('employee_service', EmployeeServiceView.as_view(), name='employee_service'),
]