from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EmployeeJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeJob
        fields = '__all__'

