from django.urls import path
from .views import *
urlpatterns = [
    path('admin', DashBoardView.as_view(), name='admin_dashboard'),

]