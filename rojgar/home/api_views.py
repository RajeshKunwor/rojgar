from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser,MultiPartParser,JSONParser,FormParser
from job.category_tree import *
from job.serializer.serializers import *

class ListServiceAPIViews(APIView):

    def get(self, request):
        category = root_category()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)

