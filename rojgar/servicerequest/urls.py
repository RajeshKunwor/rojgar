from django.urls import path
from .views import *
urlpatterns = [
    path('create_service_request', CreateServiceRequest.as_view(), name='create_service_request'),
    path('employee_list_service_request', EmployeeServiceRequestList.as_view(), name='employee_list_service_request'),
    path('client_list_service_request', ClientServiceRequestList.as_view(), name='client_list_service_request'),

]