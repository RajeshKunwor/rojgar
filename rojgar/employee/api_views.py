from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateEmployeeJobView(APIView):

    def post(self, request):
        data = request.data
        serializer = EmployeeJobSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response":"Successfully Added."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateEmployeeJobView(APIView):

    def put(self, request):
        data = request.data
        emp_job_id = data['emp_job_id']
        emp_job = EmployeeJob.objects.get(pk=emp_job_id)
        serializer = EmployeeJobSerializer(instance=emp_job, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Updated."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListEmployeeJobView(APIView):

    def get(self, request):
        emp_job = EmployeeJob.objects.all()
        serializer = EmployeeJobSerializer(emp_job, many=True)
        return Response(serializer.data)





