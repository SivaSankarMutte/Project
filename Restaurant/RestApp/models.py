from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	age=models.IntegerField(default=20)
	mobilenumber=models.CharField(max_length=10,null=True)
	uimg=models.ImageField(upload_to='Profilepics/',default='dummyProfile.png')
	t=[(1,'Guest'),(2,'Manager'),(3,'User')]
	role=models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
	f=[(2,'Manager'),(3,'User')]
	rltype=models.IntegerField(choices=f)
	pfe=models.ImageField(upload_to='Rolereqpics/',default='parota.jpg')
	is_checked=models.BooleanField(default=False)
	uname=models.CharField(max_length=50)
	ud=models.OneToOneField(User,on_delete=models.CASCADE)

class Restaurant(models.Model):
	rname=models.CharField(max_length=30)
	nitems=models.IntegerField()
	timings=models.CharField(max_length=50)
	address=models.CharField(max_length=50) 
	rsimg=models.ImageField(upload_to='RestaurantImages/')
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.rname

class Item(models.Model):
	CHOICES=[('dft','select availability'),('yes','yes'),('no','no')]
	veg_choices=[('df','Select item type'),('veg','veg'),('non-veg','non-veg')]
	itemname=models.CharField(max_length=20)
	itemtype=models.CharField(choices=veg_choices,max_length=20,default="df")
	itemprice=models.DecimalField(max_digits=6,decimal_places=2,default=100)
	itemimg=models.ImageField(upload_to='items/',default="biryani.gif")
	availability=models.CharField(choices=CHOICES,max_length=30,default=1)
	rsid=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
