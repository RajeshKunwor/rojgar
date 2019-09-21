from django.urls import path
from .api_views import *

urlpatterns = [
    path('list_service', ListServiceAPIViews.as_view(), name='list_service'),
]