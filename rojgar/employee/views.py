from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import Group, User
from django.contrib.auth import login, authenticate
from .models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from home.decorators import group_required
from rest_framework.views import APIView
# Create your views here.

@method_decorator([login_required(login_url='home:home'), group_required('employee')],name='dispatch')
class EmployeeDashboardView(View):
    def get(self, request):
        return render(request, 'employee/employee_dashboard.html')


class RegisterEmployeeView(View):



    def post(self, request):
        data = request.body.decode('UTF-8')
        emp_data = json.loads(data)
        print(emp_data)
        user_name = emp_data.get('userName')
        password1 = emp_data.get('password')
        # password2 = emp_data.get('password2')
        full_name = emp_data.get('fullName')
        mobile_number = emp_data.get('mobileNumber')
        email = emp_data.get('email')
        state = emp_data.get('state')
        district = emp_data.get('district')
        municipality = emp_data.get('municipality')
        ward_number = emp_data.get('wardNumber')
        street = emp_data.get('street')
        user = User.objects.create_user(username=user_name,password=password1)
        employee = Employee(full_name=full_name, mobile_number=mobile_number,
                            email=email, state_id=state, district_id=district, municipality_id=municipality,
                            ward_number=ward_number, street=street)
        employee.user = user
        group = Group.objects.get(name='employee')
        group.user_set.add(user)
        group.save()
        employee.save()

        authenticated_user = authenticate(username=user_name, password=password1)
        login(request, authenticated_user)
        if next:
            return render(request, 'employee/employee_dashboard.html')
        return redirect('home:home')


@method_decorator([login_required(login_url='home:home'), group_required('employee')],name='dispatch')
class EmployeeServiceView(View):

    def get(self, request):
        return render(request,'employee/employee_service.html')


@method_decorator([login_required(login_url='home:home'), group_required('employee')],name='dispatch')
class EmployeeBioView(View):

    def get(self, request):
        return render(request, 'employee/employee_bio.html')


@method_decorator([login_required(login_url='home:home'), group_required('employee')],name='dispatch')
class EmployeeDetailView(View):

    def get(self, request):
        return render(request, 'employee/employee_detail.html')


@method_decorator([login_required(login_url='home:home'), group_required('employee')],name='dispatch')
class EmployeeUpdateView(View):

    def get(self, request):
        return render(request, 'employee/update_employee.html')


@method_decorator([login_required(login_url='home:home'), group_required('employee')],name='dispatch')
class AddServiceView(View):

    def get(self, request):
        return render(request, 'employee/add_service.html')


@method_decorator([login_required(login_url='home:home'), group_required('employee')],name='dispatch')
class AddBioView(View):

    def get(self, request):
        return render(request, 'employee/add_bio.html')


@method_decorator([login_required(login_url='home:home'), group_required('employee')],name='dispatch')
class UpdateProfile(View):

    def get(self, request):
        return render(request, 'employee/update_profile.html')


@method_decorator([login_required(login_url='home:home'), group_required('employee')],name='dispatch')
class AddProfile(View):

    def get(self, request):
        return render(request, 'employee/add_profile.html')