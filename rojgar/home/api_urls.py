from django.urls import path
from .api_views import *

urlpatterns = [
    path('list_service', ListServiceAPIViews.as_view(), name='list_service'),
    path('list_employee', ListEmployeeServiceVeiw.as_view(), name='list_employee'),
    path('employee_detail', DetailEmployeeView.as_view(), name='employee_list'),
    path('search_employee', SearchEmployeeView.as_view(), name='search_employee'),
]