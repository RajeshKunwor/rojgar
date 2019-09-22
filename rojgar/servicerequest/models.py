from django.db import models
from employee.models import Employee
from client.models import Client
# Create your models here.

class ServiceRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'Service Request is sent to {self.employee} by {self.client}'


