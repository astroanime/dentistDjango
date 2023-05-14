from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Offer,Review


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
class OfferMediaForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ["cover","name","description"]
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["date_edited"]

    rating = forms.IntegerField(min_value=0, max_value=5)
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = "__all__"