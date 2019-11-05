from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser,MultiPartParser,JSONParser,FormParser
from job.category_tree import *
from job.serializer.serializers import *
from job.models import *
from employee.models import *


class ListServiceAPIViews(APIView):

    def get(self, request):
        category = root_category()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)


class ListEmployeeServiceVeiw(APIView):

    def get(self, request):
        job_id = request.GET['job_id']
        emp_service = EmployeeJob.objects.filter(job_id=job_id)
        data = []
        for e_s in emp_service:
            data.append({'emp_id': e_s.employee.id,'emp_name': e_s.employee.full_name, 'emp_mobile_number': e_s.employee.mobile_number,
                         })
        return Response(data)



class DetailEmployeeView(APIView):

    def get(self, request):
        emp_id = request.GET['emp_id']
        emp = Employee.objects.get(pk=emp_id)
        emp_address = str(emp.state.name) + ', '+ str(emp.district.name)\
                      +', '+str(emp.municipality.name)+'-'+str(emp.ward_number)+', '+str(emp.street)

        data=({'name': emp.full_name,
                     'address': emp_address,
                     'mobile_number': emp.mobile_number,
                     'email': emp.email})
        return Response(data)


class SearchEmployeeView(APIView):

    def get(self, request):
        job_id = request.GET['job_id']
        district_id = request.GET['district_id']
        emp_id = EmployeeJob.objects.filter(job_id=job_id).values('employee_id')
        emp = Employee.objects.filter(district_id=district_id).filter(id__in=emp_id)
        data = []
        for e in emp:
            data.append({'emp_id': e.id, 'emp_name': e.full_name,
                         'emp_mobile_number': e.mobile_number})


        return Response(data)

