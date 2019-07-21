from django.urls import path
from .views import *
urlpatterns = [
    path('manage-job/', ManageJobView.as_view(), name='manage_job'),
    path('manage-category/', ManageCategoryView.as_view(), name='manage_category'),
]