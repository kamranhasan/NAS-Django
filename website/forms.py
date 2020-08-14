from django import forms
from .models import Contact,Booking,MakeMyOwnTrip
from django.db import models


class Messages(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email','subject', 'message' )


class Booking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('Tour_Name', 'Your_Name','email', 'Mobile_Number', 'Number_Of_Travellers', 'message')


class MakeMyOwnTrip(forms.ModelForm):
    class Meta:
        model = MakeMyOwnTrip
        fields = ('Your_Full_Name', 'Your_Email','Your_Mobile_Number', 'Number_Of_Travellers','Departure_City' , 'Date', 'Trip_Duration', 'Enter_Locations', 'preferences')