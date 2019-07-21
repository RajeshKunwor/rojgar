from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from ..serializer.serializers import *

class CreateJobCategoryAPIView(APIView):

    def post(self, request):
        data = request.data
        serializer = JobCategorySerializer(data = data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Saved."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateJobAPIView(APIView):

    def post(self, request):
        data = request.data
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Saved."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListJobCategoryAPIView(ListAPIView):

    serializer_class = JobCategorySerializer
    queryset = Category.objects.all()


class ListJobAPIView(ListAPIView):

    serializer_class = JobSerializer
    queryset = Job.objects.all()


class UpdateJobCategoryAPIView(APIView):

    def put(self, request):
        data = request.data
        serializer = JobCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Updated."})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UpdateJobAPIView(APIView):

    def put(self, request):
        data = request.data
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Updated."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

