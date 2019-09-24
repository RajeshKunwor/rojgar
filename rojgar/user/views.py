from django.shortcuts import render
from django.views import View
# Create your views here.

class CustomerSignUpView(View):

    def get(self, request):
        return render(request, 'user/customer_signup_form.html')

class EmployeeSignupView(View):

    def get(self, request):
        return render(request, 'user/employee_signup_form.html')

class Login(View):

    def get(self, request):
        return render(request, 'user/login.html')
