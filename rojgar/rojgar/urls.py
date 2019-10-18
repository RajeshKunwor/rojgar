"""rojgar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/job/', include(('job.urls','job'), namespace='job')),
    path('api/job/', include(('job.api_urls', 'job'), namespace='job_api')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('api/home/', include(('home.api_urls', 'home'), namespace='home_api')),
    path('employee/', include(('employee.urls', 'employee'), namespace='employee')),
    path('address/', include(('address.urls', 'address'), namespace='address')),
    path('api/employee/', include(('employee.api_urls','employee'), namespace='employee_api')),

]
