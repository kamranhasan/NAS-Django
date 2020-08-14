# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Package,Testimonial
from .forms import Messages,Booking,MakeMyOwnTrip
from django.core.mail import send_mail

# Create your views here.
def index(request):
    db=Package.objects.all()
    testinomials=Testimonial.objects.all()
    form=Messages()
    respond='Send Message'
    return render(request, 'index.html',{'package': db, 'testinomials':testinomials, 'form':form,'respond':respond})

def contacted(request):
    db=Package.objects.all()
    testinomials=Testimonial.objects.all()
    if request.method=="POST":
        data=Messages(request.POST)
        if data.is_valid():
            data.save()
            send_mail('New Contact Form Submission', request.POST['message'], 'nomadsadventureservice', ['nomadsadventureservice@gmail.com'], fail_silently=False)
            respond='Your Message has been sent successfully!'
            return render(request,'index.html',{'package': db, 'testinomials':testinomials, 'data':data,'respond':respond})
        else:
            data=Messages()
            respond='Your Message has been sent successfully!'
            return render(request,'index.html',{'package': db, 'testinomials':testinomials, 'data':data,'respond':respond})


def packages(request):
    db=Package.objects.all()
    return render(request, 'destination.html',{'package': db})


def plans(request,id):
    plan=Package.objects.get(id=id)
    booking=Booking()
    respond='Book Now'
    return render(request, 'destination-single.html',{'package': plan, 'booking':booking, 'respond':respond })


def booked(request):
    # plan=Package.objects.get(id=id)
    if request.method=="POST":
        data=Booking(request.POST)
        if data.is_valid():
            data.save()
            send_mail('New Trip Booking', request.POST['Tour_Name'], 'nomadsadventureservice', ['nomadsadventureservice@gmail.com'], fail_silently=False)
            respond='You have booked yourself a tour successfully. Please make your payment and send us the transaction proof at: +92 333 1666237'
            accountDetails={"Account title" : "Nomads Adventure Services", 
                            "Iban number" :"PK88 MEZN 0001 5701 0409 4933", 
                            "Account No:" :"0157 0104094933",
                            "Bank Name":"Meezan Bank"}
            return render(request,'destination-single.html',{ 'data':data ,'respond':respond, 'accountDetails':accountDetails.keys(), 'accountDetails2':accountDetails.values() })
        else:
            data=Booking()
            respond='You have booked yourself a tour successfully. Please make your payment and send us the transaction proof at: +92 333 1666237'
            accountDetails={"Account title" : "Nomads Adventure Services", 
                            "Iban number" :"PK88 MEZN 0001 5701 0409 4933", 
                            "Account No:" :"0157 0104094933",
                            "Bank Name":"Meezan Bank"}
            return render(request,'destination-single.html',{ 'data':data ,'respond':respond, 'accountDetails':accountDetails.keys(), 'accountDetails2':accountDetails.values() })
def makemyowntrip(request):
    makemyowntrip=MakeMyOwnTrip()
    respond='Plan it For Me!'
    return render(request, 'makemyowntrip.html',{'check':'yes', 'makemyowntrip' : makemyowntrip, 'respond':respond })

def makemyowntripbooked(request):
    if request.method=="POST":
        data=MakeMyOwnTrip(request.POST)
        if data.is_valid():
            post=data.save(commit = False)
            post.save()
            send_mail('New Make My Own Trip Booking', request.POST['Your_Full_Name'], 'nomadsadventureservice', ['nomadsadventureservice@gmail.com'], fail_silently=False)
            respond='You have booked yourself a tour successfully. You will be contacted by team Nomads real quick!'
            return render(request,'makemyowntrip.html',{ 'post':post, 'check':'no' ,'respond':respond })
        else:
            data=MakeMyOwnTrip()
            respond='You have booked yourself a tour successfully. You will be contacted by team Nomads real quick!'
            return render(request,'makemyowntrip.html',{'data':data, 'check':'no' ,'respond':respond})
    else:
        respond='You have booked yourself a tour successfully. You will be contacted by team Nomads real quick!'
        return render(request,'makemyowntrip.html',{  'check':'no' ,'respond':respond })

