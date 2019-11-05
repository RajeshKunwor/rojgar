from django.urls import path
from .views import *

urlpatterns = [
    path('employee_dashboard', EmployeeDashboardView.as_view(), name='employee_dashboard'),
    path('register_employee', RegisterEmployeeView.as_view(), name='register_employee'),
    path('employee_service', EmployeeServiceView.as_view(), name='employee_service'),
    path('employee_bio', EmployeeBioView.as_view(), name='employee_bio'),
    path('employee_detail', EmployeeDetailView.as_view(), name='employee_detail'),
    path('update_employee', EmployeeUpdateView.as_view(), name='update_employee'),
]