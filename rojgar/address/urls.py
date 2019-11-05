from django.urls import path
from .views import *

urlpatterns = [
    path('load_state', LoadStateView.as_view(),name='load_state'),
    path('load_district', LoadDistrictView.as_view(),name='load_district'),
    path('load_municipality', LoadMunicipalityView.as_view(),name='load_municipality'),
    path('load_districts', LoadDistrictView1.as_view(), name='load_districts'),
]