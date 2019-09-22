from django.db import models
from django.contrib.auth.models import User
from address.models import *
from job.models import Job

# Create your models here.
class Employee(models.Model):
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


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_skill', on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.employee} | {self.skill}'


class EmployeeJob(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_job', on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name='emp_job', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee}|{self.job}'


class EmployeeHistory(models.Model):
    employee = models.ForeignKey(Employee, related_name='employee_history', on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
