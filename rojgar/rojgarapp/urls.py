from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard', DashBoard.as_view())
]