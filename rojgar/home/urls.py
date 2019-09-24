from django.urls import path
from .views import *
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('service', ServiceView.as_view(), name='service'),
    path('contact', ContactView.as_view(), name='contact'),
]