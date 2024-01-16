from django.db import models
from Admin.models import *
# Create your models here.

class Newmechanic(models.Model):
    mech_name=models.CharField(max_length=50)
    mech_contact=models.CharField(max_length=20)
    mech_email=models.EmailField(unique=True,null=True)
    mech_address=models.CharField(max_length=80)
    localplace=models.ForeignKey(Localplace, on_delete=models.CASCADE)
    mech_certificate=models.FileField(upload_to='userDocs/',)
    password=models.CharField(max_length=50,unique=True)
    doj=models.DateTimeField(auto_now_add=True,null=True)
    mech_status=models.IntegerField(default=0)
    

class Newmfb(models.Model):
    mfb_name=models.CharField(max_length=50)
    mfb_contact=models.CharField(max_length=20)
    mfb_email=models.EmailField(unique=True,null=True)
    mfb_address=models.CharField(max_length=80)
    localplace=models.ForeignKey(Localplace, on_delete=models.CASCADE)
    mfb_liscence=models.FileField(upload_to='userDocs/',)
    password=models.CharField(max_length=50,unique=True)
    doj=models.DateTimeField(auto_now_add=True,null=True)
    mfb_status=models.IntegerField(default=0)

class Newusr(models.Model):
    usr_name=models.CharField(max_length=50)
    usr_contact=models.CharField(max_length=20)
    usr_email=models.EmailField(unique=True)
    usr_address=models.TextField(null=True)
    usr_gender=models.CharField(max_length=20)
    localplace=models.ForeignKey(Localplace, on_delete=models.CASCADE)
    usr_photo=models.FileField(upload_to='userDocs/',null=True)
    usr_dob=models.DateField()
    password=models.CharField(max_length=50,unique=True)
    doj=models.DateTimeField(auto_now_add=True,null=True)

class Admindb(models.Model):
    admn_name=models.CharField(max_length = 50)
    admn_email=models.EmailField(unique=True,null=True)
    password=models.CharField(max_length=50,unique=True)