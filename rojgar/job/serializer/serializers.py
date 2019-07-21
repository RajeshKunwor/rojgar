from rest_framework import serializers
from ..models import *

class JobCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields= '__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)