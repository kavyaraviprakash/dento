from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    # birthdate = models.DateField(max_length=100)
    bloodgroup = models.CharField(max_length=5)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    #birthdate = models.DateField(max_length=100)
    bloodgroup = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    #birthdate = models.DateField(max_length=100)
    bloodgroup = models.CharField(max_length=5)
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    doctorname = models.CharField(max_length=50)
    doctoremail = models.EmailField(max_length=50)
    patientname = models.CharField(max_length=50)
    patientemail = models.EmailField(max_length=50)
    appointmentdate = models.DateField(max_length=10)
    appointmenttime = models.TimeField(max_length=10)
    symptoms = models.CharField(max_length=100)
    status = models.BooleanField(max_length=100)
    prescription = models.CharField(max_length=200)

    def __str__(self):
        return self.patientname + " you have appointment with " + self.doctorname


class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    #birthdate = models.DateField(max_length=100)
    bloodgroup = models.CharField(max_length=5)

    def __str__(self):
        return self.name
