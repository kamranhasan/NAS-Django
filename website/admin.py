# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Package,Testimonial,Contact,Booking,MakeMyOwnTrip

# Register your models here.
admin.site.register(Package)
admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(Booking)
admin.site.register(MakeMyOwnTrip)