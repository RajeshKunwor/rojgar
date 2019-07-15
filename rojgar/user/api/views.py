from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rojgar.user.models import *
from rojgar.user.serializers import *

class CreateUserAPIView(APIView):

    def post(self, request):
        data = request.data
        serializer = User(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Successfully Saved."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserProfileAPIView(APIView):

    def post(self, request):
        data = request.data
        serializer = UserProfile(data=data)
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


class UpdateUserProfileAPIView(APIView):

    def put(self, request):
        data = request.data
        id = request['id']
        user_profile = UserProfile.objects.get(id=id)
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

