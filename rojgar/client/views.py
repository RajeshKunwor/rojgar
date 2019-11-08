from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import Group, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
import json
from home.decorators import group_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


@method_decorator([login_required(login_url='home:home'), group_required('client')],name='dispatch')
class ClientDashboardView(View):

    def get(self, request):
       return render(request, 'client/client_dashboard.html')

class RegisterClientView(View):

    def get(self, request):
        pass

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
        client = Client(full_name=full_name,mobile_number=mobile_number,email=email,
                            state_id=state,district_id=district,municipality_id=municipality, ward_number=ward_number,street=street)
        client.user = user
        group = Group.objects.get(name='client')
        group.user_set.add(user)
        group.save()
        client.save()

        authenticated_user = authenticate(username=user_name, password=password1)
        login(request, authenticated_user)
        if next:
            return render(request, 'client/client_dashboard.html')
        return redirect('home:home')




