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
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(JobSerializer, self).to_representation(instance)
        rep['category'] = instance.category.name
        return rep

class JobSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'



    def create(self, validated_data):
        return Job.objects.create(**validated_data)


class RecursiveSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):
        serializer = self.parent.parent.__class__(obj)
        # print serializer
        return serializer.data


class JobSerialzers(serializers.Serializer):
    id = serializers.IntegerField()
    category = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    image = serializers.FileField()


class CategorySerializers(serializers.Serializer):
    id = serializers.IntegerField()
    parent = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    category_list = RecursiveSerializer(many=True)
    job_list = serializers.ListSerializer(child=JobSerialzers())
