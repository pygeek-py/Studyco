from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.



class movieimg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=1000000)

class list(models.Model):
	lang = models.CharField(max_length=1000)

	def __str__(self):
		return self.lang

class box(models.Model):
	host = models.ManyToManyField(movieimg)
	person = models.ForeignKey(User, on_delete=models.CASCADE)
	topic = models.CharField(max_length=10000)
	name = models.CharField(max_length=1000)
	description = models.TextField(max_length=1000000)
	based = models.ForeignKey(list, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

class talk(models.Model):
    join = models.ForeignKey(box, on_delete=models.CASCADE)
    people = models.ForeignKey(User, on_delete=models.CASCADE)
    host = models.ManyToManyField(movieimg)
    text = models.CharField(max_length=3000)
    day = models.DateTimeField(auto_now_add=True)


class enter(models.Model):
	boxper = models.ForeignKey(User, on_delete=models.CASCADE)
	boxen = models.ManyToManyField(box)

class followercount(models.Model):
	follower = models.CharField(max_length=1000)
	user = models.CharField(max_length=1000)

	def __str__(self):
		return self.user