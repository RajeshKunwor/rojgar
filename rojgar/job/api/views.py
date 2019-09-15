from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from ..serializer.serializers import *
from rest_framework.parsers import FileUploadParser,MultiPartParser,JSONParser,FormParser
from ..category_tree import root_category

class CreateJobCategoryAPIView(APIView):

    def post(self, request):
        data = request.data
        serializer = JobCategorySerializer(data = data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Saved."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateJobAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        data = request.data
        print(data)
        serializer = JobSerializer(data=data)
        print (serializer)
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
        category_id = data['category_id']
        category = Category.objects.get(id=category_id)
        serializer = JobCategorySerializer(instance=category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Updated."})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UpdateJobAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def put(self, request):
        data = request.data
        print(data.get('id'))
        job_id = data.get('id')
        job = Job.objects.get(id=job_id)
        serializer = JobSerializer(instance=job,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Updated."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCategoryAPIViews(APIView):

    def get(self, request):
        category = root_category()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)


class GetJob(APIView):

    def get(self, request):
        job_id = request.GET.get('job')
        job = Job.objects.get(id=job_id)
        serializer = JobSerializer1(job)
        return Response(serializer.data)