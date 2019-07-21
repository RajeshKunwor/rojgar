from django.urls import path
from .api.views import *

urlpatterns = [
    path('create_job', CreateJobAPIView.as_view(), name='create_job'),
    path('create_category', CreateJobCategoryAPIView.as_view(), name='create_category'),
    path('list_category', ListJobCategoryAPIView.as_view(), name='list_category'),
    path('list_job', ListJobAPIView.as_view(), name='list_job'),
    path('update_category', UpdateJobCategoryAPIView.as_view(), name='update_category'),
    path('update_job', UpdateJobAPIView.as_view(), name='update_job')
]

