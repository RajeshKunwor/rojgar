from django.urls import path
from .views import *
urlpatterns = [
    path('manage-job/', ManageJobView.as_view(), name='manage_job'),
    path('manage-category/', ManageCategoryView.as_view(), name='manage_category'),
    path('create-job/', CreateJobView.as_view(), name='create_job'),
    path('create-category/', CreateCategoryView.as_view(), name='create_category'),
    path('update-job', UpdateJobView.as_view(), name='update_job'),
]