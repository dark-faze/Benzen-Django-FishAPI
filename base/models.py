from django.db import models
from os import path

# Create your models here.

class Record(models.Model):
    def nameFile(instance, filename):
      if(path.isfile('/'.join(['images', str(instance.name), filename]))):
         return NULL
      else:
         return '/'.join(['images', str(instance.name), filename])
    name = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    weight = models.IntegerField()
    length = models.IntegerField()
    image = models.ImageField(upload_to=nameFile,blank=True);
    latitude = models.DecimalField(max_digits=10,decimal_places=3)
    longitude = models.DecimalField(max_digits=10,decimal_places=3)
    timestamp = models.DateTimeField(auto_now_add = True)



