from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user_photo')
    photo = models.FileField(upload_to='media', blank=True,null=True)