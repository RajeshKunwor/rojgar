from django.urls import path
from .api_views import *

urlpatterns = [
    path('list_employee', ListEmployeeView.as_view(), name='list_employee'),
    path('get_employee', GetEmployeeView.as_view(), name='get_employee'),
    path('create_employee_job', CreateEmployeeJobView.as_view(), name='create_employee_job'),
    path('update_employee_job', UpdateEmployeeJobView.as_view(), name='update_employee_job'),
    path('list_employee_job', ListEmployeeJobView.as_view(), name='list_employee_job'),
    path('create_employee_bio', CreateEmployeeBioView.as_view(), name='create_employee_bio'),
    path('update_employee_bio', UpdateEmployeeBioView.as_view(), name='update_employee_bio'),
    path('list_employee_bio', ListEmployeeJobView.as_view(), name='list_employee_bio'),
    path('get_employee_service', GetEmployeeServiceView.as_view(), name='get_employee_service'),
]