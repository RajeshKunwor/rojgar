from django.urls import path
from .api_views import *

urlpatterns = [
    path('create_service_request', CreateServiceRequestView.as_view(), name='create_service_request'),
    path('update_service_request', UpdateServiceRequestView.as_view(), name='update_service_request'),
    path('list_service_request', ListServiceRequestView.as_view(), name='list_service_request')
]