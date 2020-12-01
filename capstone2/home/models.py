from django.db import models
from django.utils.text import slugify


class PatientInfo(models.Model):
    id_patient =models.CharField(max_length=200)
    age= models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    national= models.CharField(max_length=200)
    description= models.TextField()
    id_popup=  models.IntegerField(default=0)

    def __str__(self):
        return self.id_patient

class NewsInfo(models.Model):
    title=models.CharField(max_length=500)
    link=models.CharField(max_length=500)
    image=models.CharField(max_length=500)
    content=models.CharField(max_length=500)
    date=models.CharField(max_length=500)

    def __str__(self):
        return self.title

class DirectingInfo(models.Model):
    date=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    title=models.CharField(max_length=500)
    content=models.CharField(max_length=500)
    effect=models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class DictricStatictisInfo(models.Model):
    address=models.CharField(max_length=500)
    socanhiem = models.IntegerField(default=0)
    dangdieutri=models.IntegerField(default=0)
    khoi=models.IntegerField(default=0)
    tuvong=models.IntegerField(default=0)

    def __str__(self):
        return self.address

class DirectingNewsInfo(models.Model):
    title=models.CharField(max_length=500)
    link=models.CharField(max_length=500)
    image=models.CharField(max_length=500)
    content=models.CharField(max_length=500)
    date=models.CharField(max_length=500)

    def __str__(self):
        return self.title
