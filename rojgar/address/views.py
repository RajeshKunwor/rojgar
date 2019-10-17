from django.shortcuts import render
from django import views
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
class LoadStateView(views.View):


    def get(self, reqeust):
        state = State.objects.all().values()

        data = list(state)


        return JsonResponse(data, safe=False)


class LoadDistrictView(views.View):


    def get(self, request):
        # state = request.GET.get('state')
        state = request.GET.get('state')

        district = District.objects.filter(state_id=state).values()

        data = list(district)


        return JsonResponse(data, safe=False)



class LoadMunicipalityView(views.View):


    def get(self, request):
        # state = request.GET.get('state')
        district = request.GET.get('district')

        muni = Municipality.objects.filter(district_id=district).values()

        data = list(muni)


        return JsonResponse(data, safe=False)
