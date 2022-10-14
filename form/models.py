from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    pin = models.IntegerField()
    house = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    visit = models.CharField(max_length=30)
    