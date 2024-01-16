from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class Repairschedule(models.Model):
    mechid=models.ForeignKey(Newmechanic,on_delete=models.CASCADE)
    uid=models.ForeignKey(Newusr,on_delete=models.CASCADE)
    current_location=models.CharField(max_length=120)
    landmark=models.CharField(max_length=50)
    veh_brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    model_name=models.CharField(max_length=50)
    model_year=models.CharField(max_length=50)
    issue_note=models.CharField(max_length=120)
    dt_of_booking=models.DateTimeField(auto_now_add=True)
    booking_status=models.IntegerField(default=0)

class Mfbschedule(models.Model):
    mfbid=models.ForeignKey(Newmfb,on_delete=models.CASCADE)
    usrid=models.ForeignKey(Newusr,on_delete=models.CASCADE)
    current_location=models.CharField(max_length=120)
    landmark=models.CharField(max_length=50)
    vehicle_type=models.ForeignKey(Vehicletype,on_delete=models.CASCADE)
    fuel_type=models.CharField(max_length=50)
    fuel_amount=models.CharField(max_length=50,default=0)
    dt_of_booking=models.DateTimeField(auto_now_add=True)
    mfbbooking_status=models.IntegerField(default=0)

class Usrfeedback(models.Model):
    usrid=models.ForeignKey(Newusr, on_delete=models.CASCADE)
    feedback=models.CharField(max_length = 500)
    dt_of_feedback=models.DateTimeField(auto_now_add=True)
    

class Usrcomplaint(models.Model):
    usrid=models.ForeignKey(Newusr, on_delete=models.CASCADE)
    complaint=models.CharField(max_length = 500)
    dt_of_compreg=models.DateTimeField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0,null=True)
    complaint_response=models.CharField(max_length=200,null=True)