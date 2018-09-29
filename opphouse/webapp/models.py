from django.db import models
from django.contrib.auth.models import User



class Donor(models.Model):
	first_name	=models.CharField(max_length=50)
	last_name	=models.CharField(max_length=50)

	phone		=models.CharField(max_length=20)
	address		=models.CharField(max_length=100)
	email 		=models.EmailField()

	otherinfo	=models.TextField(blank=True)

	@property #automatically updated value strname
	def strname(self):
		self._strname=self.last_name+', '+self.first_name
		return self._strname
	
	def __str__(self):#text displayed
		return self.strname


class Car(models.Model):
	donor 		=models.ForeignKey('Donor',on_delete=models.CASCADE)
	
	vin			=models.CharField(max_length=17) #autocheck vin?
	mileage		=models.DecimalField(decimal_places=1,max_digits=10)
	
	year		=models.IntegerField()
	make		=models.CharField(max_length=30)
	carmodel	=models.CharField(max_length=30)

	extrainfo	=models.TextField()


class Event(models.Model):#attachable associated documents?
	eventname	=models.CharField(max_length=50)

	startdate	=models.DateTimeField()
	enddate		=models.DateTimeField(help_text="Must be same or after startdate")#verify that is after startdate

	price		=models.SmallIntegerField(default=0)
	img 		=models.ImageField(blank=True)
	loc			=models.TextField()

	def __str__(self):
		return self.eventname



class Sponsor(models.Model):
	sponsorname	=models.CharField(max_length=100)
	url 		=models.URLField()
	pic 		=models.ImageField()

	def __str__(self):
		return self.sponsorname



class Pickup(models.Model):
	donor 		=models.ForeignKey('Donor',on_delete=models.CASCADE)#if donor is deleted, all pickups for donor are deleted as well
	
	submitdate 	=models.DateTimeField(auto_now_add=True)
	items		=models.TextField()

	specinstruct=models.TextField(blank=True)
	imgs		=models.ImageField(blank=True)

	trip 		=models.ForeignKey('Trip',on_delete=models.SET_NULL,null=True,blank=True)
class Trip(models.Model):
	#__str__ shows date, {dump: Dump Run,pd: x Stop ~Pickup~ Run}
	scheduleddate=models.DateTimeField() 
	driver		=models.CharField(max_length=100)

	TRIPTYPE_CHOICES=(
		('PD','Pickup/Dropoff'),
		('DMP','Dump Run'))

	triptype 	=models.CharField(max_length=3,choices=TRIPTYPE_CHOICES,default='PD')

# class Sale(models.Model):

# 	salecats 	=models.TextField(max_length=50)
# 	saleamt		=models.TextField(max_length=50)#make into flexible types? (x% off, $y off, buy z get $q etc etc etc - match epos?)

# 	saledesc	=models.CharField(max_length=100) #shows in different page or smth? 
# 	salestart	=models.DateTimeField()
# 	saleend		=models.DateTimeField()

