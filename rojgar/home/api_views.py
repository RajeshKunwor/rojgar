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
            data.append({'emp_id': e_s.id,'emp_name': e_s.employee.full_name, 'emp_mobile_number': e_s.employee.mobile_number,
                         'emp_photo': e_s.employee.user.photo})
        return Response(data)



