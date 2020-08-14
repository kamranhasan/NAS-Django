# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
# Create your models here.
class Package(models.Model):
    name=models.CharField(max_length=300)
    picture=models.ImageField()
    price=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    date=models.DateField()
    days=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    departure=models.CharField(max_length=100)
    departureTime=models.TimeField()
    returnTime=models.TimeField()
    included=models.CharField(max_length=300)
    notIncluded=models.CharField(max_length=300,default='')
    # itinerary=models.CharField(max_length=1000,default='')
    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name=models.CharField(max_length=300)
    picture=models.ImageField()
    description=models.CharField(max_length=400)
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=400)
    def __str__(self):
        return self.name

class Booking(models.Model):
    Tour_Name=models.CharField(max_length=150)
    Your_Name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    Mobile_Number=models.CharField(max_length=50)
    Number_Of_Travellers=models.IntegerField(null=True)
    message=models.CharField(max_length=400,default='')
    def __str__(self):
        return self.Tour_Name

class MakeMyOwnTrip(models.Model):
    CITIES = (
        ('KH', 'Karachi'),
        ('ISL', 'Islamabad'),
        ('LH', 'Lahore')
    )
    Your_Full_Name=models.CharField(max_length=150)
    Your_Email=models.CharField(max_length=150)
    Your_Mobile_Number=models.CharField(max_length=100)
    Number_Of_Travellers=models.IntegerField(null=True)
    Departure_City=models.CharField(max_length=100, choices=CITIES)
    Date=models.DateField()
    Trip_Duration=models.IntegerField(null=True)
    Enter_Locations=models.CharField(max_length=500)
    preferences=models.CharField(max_length=400)
    def __str__(self):
        return self.Your_Full_Name