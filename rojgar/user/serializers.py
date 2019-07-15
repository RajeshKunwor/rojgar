from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        exclude ='id'
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields ='__all__'
