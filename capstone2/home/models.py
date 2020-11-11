from django.db import models
from django.utils.text import slugify


class PatientInfo(models.Model):
    id_patient =models.CharField(max_length=200)
    age= models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    national= models.CharField(max_length=200)

    def __str__(self):
        return self.id_patient

