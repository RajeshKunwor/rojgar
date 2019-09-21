from django.urls import path
from .views import *
urlpatterns = [
    path('customer-signup', CustomerSignUpView.as_view(), name='customer_signup'),

]