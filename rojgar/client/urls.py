from django.urls import path
from .views import *

urlpatterns = [
    path('client_dashboard', ClientDashboardView.as_view(), name='client_dashboard'),
    path('register_client', RegisterClientView.as_view(), name='register_client'),

]