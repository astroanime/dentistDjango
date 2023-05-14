from django.contrib import admin
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Register your models here.
from .models import Customer, Appointment, Stuff,Servise,Offer,Review,Doctor,Article,Profile
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(Stuff)
admin.site.register(Servise)
admin.site.register(Offer)
admin.site.register(Review)
admin.site.register(Doctor)
admin.site.register(Article)
admin.site.register(Profile)
