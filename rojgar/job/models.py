from django.db import models
from mptt.models import TreeForeignKey,MPTTModel
# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name}'


class Job(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='job_category')
    description = models.TextField()
    photo = models.FileField(upload_to='job_photo', null=True, blank=True)

    def __str__(self):
        return f'{self.category}|{self.name}'



