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

    def __str__(self):
        return self.user.username

class Location(models.Model):
    name = models.CharField(max_length=50, default="")
    longitude = models.DecimalField(default=16.566,max_digits=8, decimal_places=3)
    latitude = models.DecimalField(default=81.522,max_digits=8, decimal_places=3)

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=20, default="")
    facultyCoordinator = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name="facultyCord")
    studentCoordinator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="studentCord")
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    totalPraticipants = models.IntegerField()
    isSpot = models.BooleanField(default=True)
    department = models.CharField(max_length=5,default="CSE")
    def __str__(self):
        return self.name

class Participations(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    registeredOn = models.DateTimeField(auto_now_add=True)
