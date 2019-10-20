from django.urls import path
from .views import *
urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout',signout, name='logout'),
    path('customer-signup', CustomerSignUpView.as_view(), name='customer_signup'),
    path('employee-signup', EmployeeSignupView.as_view(), name='employee_signup'),

]