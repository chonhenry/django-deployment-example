from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	email = models.CharField(max_length=264, unique=True)

	def __str__(self):
		return self.first_name

class UserProfileInfo(models.Model):
	# create relationship (don't inherit from User!)
	user = models.OneToOneField(User, on_delete=models.PROTECT)

	# Add any additional attributes you want
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

	def __str__(self):
		# Built-in attribute of django.contrib.auth.models.User
		return self.user.username


