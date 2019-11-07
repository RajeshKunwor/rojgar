from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=10, default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)


class State(models.Model):
    name = models.CharField(max_length=254)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.country}|{self.name}'


class District(models.Model):
    name = models.CharField(max_length=254)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.state}|{self.name}'


class Municipality(models.Model):
    name = models.CharField(max_length=254)
    district = models.ForeignKey(District, related_name='municipality',on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Ward(models.Model):
    number = models.IntegerField()
    municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.municipality}|{self.number}'