from django.db import models

# Create your models here.
class State(models.Model):
    state_name=models.CharField(max_length=50)
    def __str__(self):
        return self.state_name

class District(models.Model):
    district_name=models.CharField(max_length=50)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.district_name
    
class Vehicletype(models.Model):
    vehicle_type=models.CharField(max_length=50)
    def __str__(self):
        return self.vehicle_type

class Brand(models.Model):
    brand_name=models.CharField(max_length=50)
    vehicle_type=models.ForeignKey(Vehicletype,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.brand_name

class Place(models.Model):
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    place_name=models.CharField(max_length=50)

    def __str__(self):
        return self.place_name

class Localplace(models.Model):
    place=models.ForeignKey(Place, on_delete=models.CASCADE)
    local_place=models.CharField(max_length=50)

    def __str__(self):
        return self.local_place