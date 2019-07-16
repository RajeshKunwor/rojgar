from django.conf import settings
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name= 'login'),
    ]