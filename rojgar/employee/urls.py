from django.urls import path
from .views import *

urlpatterns = [
    path('employee_dashboard', EmployeeDashboardView.as_view(), name='employee_dashboard')
]