
from django.db import models

# Create your models here.

class job(models.Model):
    job_name=models.CharField(max_length=255,null=True)
    job_description=models.CharField(max_length=255,null=True)
    qualification=models.CharField(max_length=255,null=True)
    skills=models.CharField(max_length=255,null=True)
    salary=models.CharField(max_length=255,null=True)

class emplayee(models.Model):
    applied_job=models.CharField(max_length=255,null=True)
    name=models.CharField(max_length=255,null=True)
    email=models.CharField(max_length=255,null=True)
    phon_number=models.IntegerField(null=True)
    file = models.FileField(upload_to="uploaded_files/",blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True)


class sign(models.Model):
    username=models.CharField(max_length=255,null=True)
    email=models.EmailField(null=True)
    password1=models.CharField(max_length=255,null=True)
    password2=models.CharField(max_length=255,null=True)

class user_login(models.Model):
    username=models.CharField(max_length=255,null=True)
    password=models.CharField(max_length=255,null=True)