from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import Group, User
from django.contrib.auth import login, authenticate, logout
import json
# Create your views here.

def hasGroup(user, groupName):
    group = Group.objects.get(name=groupName)
    return True if group in user.groups.all() else False


class CustomerSignUpView(View):

    def get(self, request):
        return render(request, 'user/customer_signup_form.html')

class EmployeeSignupView(View):

    def get(self, request):
        return render(request, 'user/employee_signup_form.html')

class Login(View):

    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        data = request.body.decode('UTF-8')
        user_data = json.loads(data)
        user_name = user_data.get('userName')
        password = user_data.get('password')
        authenticated_user = authenticate(username=user_name, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            if next:
                if hasGroup(request.user, 'employee'):
                    return JsonResponse({"response":"http://127.0.0.1:4000/employee/employee_dashboard"})

                elif hasGroup(request.user, 'client'):
                    return JsonResponse({"response": 'http://127.0.0.1:4000/client/client_dashboard'})

                elif hasGroup(request.user, 'admin'):
                   return JsonResponse({"response":"http://127.0.0.1:4000/dashboard/admin"})

        else:
            return JsonResponse({"response": "UserName or Password is incorrect !"})


def dashbaord(request):
    if hasGroup(request.user, 'employee'):
        print(request.user)
        return render(request, 'employee/employee_dashboard.html')

    elif hasGroup(request.user, 'client'):
        return render(request, 'client/client_dashboard.html')

    elif hasGroup(request.user, 'admin'):
        return render(request, 'dashboard/admin_dashboard.html')


def signout(request):
    logout(request)
    return redirect('home:home')