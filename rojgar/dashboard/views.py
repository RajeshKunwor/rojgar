from django.shortcuts import render
from django.views import View
from home.decorators import group_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator([login_required(login_url='home:home'), group_required('admin')],name='dispatch')
class DashBoardView(View):

    def get(self, request):
        return render(request, 'dashboard/admin_dashboard.html')


