from django.db import models

# Create your models here.

class Patients(models.Model):
    name= models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    age= models.IntegerField()
    address= models.CharField(max_length=200)


    def __str__(self):
        return self.name