from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from user.models import *
from ..serializers import *
import json
from rest_framework.parsers import FileUploadParser,MultiPartParser,JSONParser,FormParser

class CreateUserAPIView(APIView):

    def post(self, request):
        data = request.data
        print(data)
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Saved."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserProfileAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        data = request.data
        print(data)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Saved."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListUserAPIView(ListAPIView):

    serializer_class = User
    queryset = User.objects.all()


class ListUserProfileAPIView(ListAPIView):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class GetUserProfileAPIView(APIView):

    def get(self, request):
        user_id = request.GET['user_id']
        user_profile = UserProfile.objects.get(user_id=user_id)
        data = {'image': user_profile.photo.url }
        return Response(data)


class UpdateUserProfileAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def put(self, request):
        data = request.data
        id = request['user_id']
        user_profile = UserProfile.objects.get(user_id=id)
        serializer = UserProfileSerializer(instance=user_profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Updated."})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UpdateUserAPIView(APIView):

    def put(self, request):
        data = request.data
        id = request['id']
        user = User.objects.get(id=id)
        serializer = UserSerializer(instance=user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Updated."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

