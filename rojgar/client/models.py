from django.db import models
from django.db import models
from django.contrib.auth.models import User
from address.models import *
from job.models import Job

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User,related_name='user_emp', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    state = models.OneToOneField(State, related_name='employee_state', on_delete=models.CASCADE)
    district = models.OneToOneField(District, related_name='employee_district', on_delete=models.CASCADE)
    municipality = models.OneToOneField(Municipality, related_name='employee_municipality', on_delete=models.CASCADE)
    ward_number = models.OneToOneField(Ward, related_name='employee_ward', on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'{self.full_name}'

