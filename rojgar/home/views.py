from django.shortcuts import render
from django.views import View
# Create your views here.

class Home(View):

    def get(self, request):
        return render(request, 'home/home.html')

class ServiceView(View):

    def get(self, request):
        return render(request, 'home/service.html')


class ContactView(View):

    def get(self, request):
        return render(request, 'home/contact.html')