from django.shortcuts import render
from django.views import View
from home.decorators import group_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator([login_required(login_url='home:home'), group_required('admin')],name='dispatch')
class ManageJobView(View):

    def get(self, request):
        return render(request, 'job/manage_job.html')


@method_decorator([login_required(login_url='home:home'), group_required('admin')],name='dispatch')
class ManageCategoryView(View):

    def get(self, request):
        return render(request, 'job/manage_category.html')


@method_decorator([login_required(login_url='home:home'), group_required('admin')],name='dispatch')
class CreateCategoryView(View):

    def get(self, request):
        return render(request, 'job/category_form.html')


@method_decorator([login_required(login_url='home:home'), group_required('admin')],name='dispatch')
class CreateJobView(View):

    def get(self, request):
        return render(request, 'job/job_forms.html')


@method_decorator([login_required(login_url='home:home'), group_required('admin')],name='dispatch')
class UpdateJobView(View):

    def get(self, request):
        return render(request, 'job/job_forms.html')
