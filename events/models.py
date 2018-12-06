from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField()
    college = models.CharField(max_length=30,default="")
    joinedOn = models.DateTimeField(auto_now_add=True)
    isCoordinator = models.BooleanField(default=False)
    isFaculty = models.BooleanField(default=False) 

class Location(models.Model):
    name = models.CharField(max_length=50, default="")
    longitiude = models.DecimalField(max_digits=8, decimal_places=3)
    latitude = models.DecimalField(max_digits=8, decimal_places=3)

class Events(models.Model):
    name = models.CharField(max_length=20, default="")
    facultyCoordinator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="facultyCord")
    studentCooordinator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="studentCord")
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    totalPraticipants = models.IntegerField()
    isSpot = models.BooleanField(default=True)


class Participations(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    registeredOn = models.DateTimeField(auto_now_add=True)
