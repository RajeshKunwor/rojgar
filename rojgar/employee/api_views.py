from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ListEmployeeView(APIView):

    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)


class GetEmployeeView(APIView):

    def get(self, request):
        emp_id = request.GET['emp_id']
        employee = Employee.objects.get(id=emp_id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

class CreateEmployeeJobView(APIView):

    def post(self, request):
        data = request.data
        serializer = EmployeeJobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"Successfully Added."})
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


class CreateEmployeeBioView(APIView):

    def post(self, request):
        data = request.data
        serializer = EmployeeBioSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response":"Successfully Saved."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateEmployeeBioView(APIView):

    def put(self, request):
        data = request.data
        emp_bio_id = data['emp_bio_id']
        emp_bio = EmployeeBio.objects.get(pk=emp_bio_id)
        serializer = EmployeeBioSerializer(instance=emp_bio, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Updated."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListEmployeeBioView(APIView):

    def get(self, request):
        emp_bio = EmployeeBio.objects.all()
        serializer = EmployeeJobSerializer(emp_bio, many=True)
        return Response(serializer.data)


class DetailEmployeeDetailView(APIView):

    def get(self, request):
        emp_id = request.GET['empId']
        emp = Employee.objects.get(pk=emp_id)
        serializer = EmployeeJobSerializer(emp)
        return Response(serializer.data)


class GetEmployeeServiceView(APIView):

    def get(self, request):
        emp_id = request.GET['emp_id']
        emp_service = EmployeeJob.objects.filter(employee_id=emp_id)
        data = []
        for es in emp_service:
            data.append({'service_name':es.job.name})

        return Response(data)
