from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	CATEGORY = (
			('RICH', 'POOR'),
			('ЧАСТЫЕ', 'РЕДКИЕ'),
			)

	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	emails = models.CharField(max_length=200, null=True)
	date_created = models.TimeField(auto_now_add=True, null=True)
	cover = models.ImageField(null=True,blank=True,upload_to="user_profile/")
	def __str__(self):
		return self.name +" " + self.phone + " " + self.emails

class Offer(models.Model):
	cover = models.ImageField(null=True,blank=True,upload_to="offer_profile/")
	name = models.CharField(max_length=30,null=True)
	description = models.CharField(max_length=200,null=True)
	def __str__(self):
		return self.name +" " + self.description

class Stuff(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	emails = models.CharField(max_length=200, null=True)
	date_created = models.TimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.name +" " + self.phone + " " + self.emails

class Appointment(models.Model):
	service = models.CharField(max_length=200, null=True)
	stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.service
class Appointment(models.Model):
	neme = models.CharField(max_length=20, null=True)
class Servise(models.Model):
	name = models.CharField(max_length=40, default=None)
	quantity = models.IntegerField(default=1)
	price = models.IntegerField(default=10)
	def __str__(self):
		return self.name

class Article(models.Model):
	name = models.CharField(max_length=50,null=False)
	content = models.CharField(max_length=50,null=False)
	image = models.ImageField(null=True,blank=True,upload_to="article_image/")
	date_created = models.DateTimeField(auto_now_add=True)
	a_link = models.URLField(null=True)
	def __str__(self):
		return self.name + " " + self.content
class Review(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The the reviewer has given.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(null=True,
                                       help_text="The date and time the review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.creator) + " " + str(self.article)
class Doctor(models.Model):
	name = models.CharField(max_length=50,null=False)
	proffesion = models.CharField(max_length=50,null=False)
	image = models.ImageField(null=True,blank=True,upload_to="doctor_profile/")
	f_link = models.URLField()
	i_link = models.URLField()
	g_link = models.URLField()
	def __str__(self):
		return self.name + " " + self.proffesion
	
class Profile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to="users_profile/")
    def __str__(self):
	    return str(self.user)
    