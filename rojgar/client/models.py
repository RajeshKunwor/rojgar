from django.db import models
from django.db import models
from django.contrib.auth.models import User
from address.models import *
from job.models import Job

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User,related_name='user_client', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    state = models.ForeignKey(State, related_name='client_state', on_delete=models.CASCADE)
    district = models.ForeignKey(District, related_name='client_district', on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, related_name='client_municipality', on_delete=models.CASCADE)
    ward_number = models.IntegerField()
    street = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'{self.full_name}'

