from django.shortcuts import render
from django.views import View
# Create your views here.

class ManageJobView(View):

    def get(self, request):
        return render(request, 'job/manage_job.html')


class ManageCategoryView(View):

    def get(self, request):
        return render(request, 'job/manage_category.html')