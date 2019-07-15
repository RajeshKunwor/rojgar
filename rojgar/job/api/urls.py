from django.urls import path

from .views import *

urlpatterns = [
    path('api/create_job', CreateJobAPIView.as_view(), name='create_job'),
    path('api/create_category', CreateJobCategoryAPIView.as_view(), name='create_category'),
    path('api/list_category', ListJobCategoryAPIView.as_view(), name='list_category'),
    path('api/list_job', ListJobAPIView.as_view(), name='list_job'),
    path('api/update_category', UpdateJobCategoryAPIView.as_view(), name='update_category'),
    path('api/update_job', UpdateJobAPIView.as_view(), name='update_job')
]

