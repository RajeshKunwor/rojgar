from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import Group, User
from django.contrib.auth import login, authenticate
from .models import *
# Create your views here.

class EmployeeDashboardView(View):
    def get(self, request):
        return render(request, 'employee/employee_dashboard.html')


class RegisterEmployeeView(View):



    def post(self, request):
        print(request.POST)
        # user_name = request.POST.get('user_name')
        # password1 = request.POST.get('password')
        # password2 = request.POST.get('password2')
        # full_name = request.POST.get('full_name')
        # mobile_number = request.POST.get('mobile_number')
        # email = request.POST.get('email')
        # state = request.POST.get('state')
        # district = request.POST.get('district')
        # municipality = request.POST.get('municipality')
        # street = request.POST.get('street')
        # user = User.objects.create_user(username=user_name,password=password1)
        # employee = Employee(full_name=full_name,mobile_number=mobile_number,email=email,
        #                     state=state,district=district,municipality=municipality,street=street)
        # employee.user = user
        # group = Group.objects.get(name='employee')
        # group.user_set.add(user)
        # group.save()
        # employee.save()
        #
        # authenticated_user = authenticate(username=user_name, password=password1)
        # login(request, authenticated_user)
        return redirect('home:home')




