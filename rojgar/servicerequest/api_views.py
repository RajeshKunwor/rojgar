from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from .models import *

class CreateServiceRequestView(APIView):

    def post(self, request):
        data = request.data
        serializer = ServiceRequestSerializer(data=data, many=True)
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


class ListServiceRequestView(APIView):

    def get(self, request):
        service_request = ServiceRequest.objects.all()
        serializer = ServiceRequestSerializer(service_request)
        return Response(serializer.data)


