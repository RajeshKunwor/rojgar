from django.shortcuts import render
from django.views import View

# Create your views here.

class CreateServiceRequest(View):

    def get(self, request):
        return render(request, 'servicerequest/service_request_form.html')


class EmployeeServiceRequestList(View):

    def get(self, request):
        return render(request, 'servicerequest/employee_service_request_list.html')

class ClientServiceRequestList(View):

    def get(self, request):
        return render(request, 'servicerequest/client_service_request_list.html')