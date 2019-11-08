from django.urls import path
from .api.views import *

urlpatterns = [
    path('create_profile', CreateUserProfileAPIView.as_view(), name='create_profile'),
    path('update_profile', UpdateUserProfileAPIView.as_view(), name='update_profile'),
    path('list_profile', ListUserProfileAPIView.as_view(), name='list_profile'),
    path('get_profile', GetUserProfileAPIView.as_view()),
]

