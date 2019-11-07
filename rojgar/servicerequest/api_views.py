from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from .models import *

class CreateServiceRequestView(APIView):

    def post(self, request):
        data = request.data
        print(data)
        serializer = ServiceRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Sent."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateServiceRequestView(APIView):

    def put(self, request):
        data = request.data
        service_request_id = data['serviceRequestId']
        service_request = ServiceRequest.objects.get(pk=service_request_id)
        serializer = ServiceRequestSerializer(instance=service_request, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Updated."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListServiceRequestViews(APIView):

    def get(self, request):
        service_request = ServiceRequest.objects.all()
        serializer = ServiceRequestSerializer(service_request)
        return Response(serializer.data)



class ListServiceRequestView(APIView):

    def get(self, request):
        emp_id = request.GET['emp_id']
        service_request = ServiceRequest.objects.filter(employee_id=emp_id).filter(status='pending')
        data = []
        for sr in service_request:
            client_address = str(sr.client.district.name)+\
                             ', '+str(sr.client.municipality.name)+'-'+str(sr.client.ward_number)+' ,'+str(sr.client.street)

            data.append({ 'id': sr.id,'client_name': sr.client.full_name, 'client_address': client_address,
                         'client_contact': sr.client.mobile_number, 'description': sr.description})

        return Response(data)


class ListClientServiceRequestView(APIView):

    def get(self, request):
        client_id = request.GET['client_id']
        service_request = ServiceRequest.objects.filter(client_id=client_id)
        data = []
        for sr in service_request:
            employee_address = str(sr.employee.district.name) + \
                             ', ' + str(sr.employee.municipality.name) + '-' + str(sr.employee.ward_number) + ' ,' + str(
                sr.employee.street)

            data.append({'id': sr.id, 'employee_name': sr.employee.full_name, 'employee_address': employee_address,
                         'employee_contact': sr.employee.mobile_number, 'description': sr.description, 'status': sr.status})

        return Response(data)

class UpdateStatusView(APIView):

    def post(self, request):
        data = request.data
        service_request_id = data['service_request_id']
        service_request = ServiceRequest.objects.get(id=service_request_id)
        service_request.status = 'confirmed'
        service_request.save()
        return Response({'response': 'Successfully Confirmed.'})