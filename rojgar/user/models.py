from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_profile')
    photo = models.FileField(upload_to='profile_photo', blank=True,null=True)