from rest_framework import serializers
from rest_framework import status
from .models import *

class ServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceRequest
        fields = '__all__'
