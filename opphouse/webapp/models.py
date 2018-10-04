from django.db import models
from django.contrib.auth.models import User



class Donor(models.Model):
	first_name	=models.CharField(max_length=50)
	last_name	=models.CharField(max_length=50)

	phone		=models.CharField(max_length=20)
	address		=models.CharField(max_length=100)#break address into separate fields
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
	mileage		=models.DecimalField(decimal_places=1,max_digits=10)#multiple choice
	
	year		=models.IntegerField()
	make		=models.CharField(max_length=30)
	carmodel	=models.CharField(max_length=30)
	#does it run/have the title needed
	extrainfo	=models.TextField(blank=True)


class Event(models.Model):#attachable associated documents?
	eventname	=models.CharField(max_length=50)

	startdate	=models.DateTimeField()
	enddate		=models.DateTimeField(help_text="Must be same or after startdate")#verify that is after startdate

	price		=models.SmallIntegerField(default=0)
	img 		=models.ImageField(blank=True,upload_to='eventimages/')
	loc			=models.TextField()

	eventdesc	=models.TextField(blank=True)

	url 		=models.URLField(blank=True)
	fblink 		=models.URLField(blank=True)
	def __str__(self):
		return self.eventname



class Sponsor(models.Model):
	sponsorname	=models.CharField(max_length=100)
	url 		=models.URLField()
	pic 		=models.ImageField(blank=True,upload_to='sponsorimages/')
	SPONSOR_TYPES=(
		('MJ','Major Sponsor'),
		('SP','Sponsored by'))
	sponsortype =models.CharField(max_length=2,choices=SPONSOR_TYPES,default='SP')
	def __str__(self):
		return self.sponsorname



class Pickup(models.Model):
	donor 		=models.ForeignKey('Donor',on_delete=models.CASCADE)#if donor is deleted, all pickups for donor are deleted as well
	
	submitdate 	=models.DateTimeField(auto_now_add=True)
	items		=models.TextField()

	specinstruct=models.TextField(blank=True)
	imgs		=models.ImageField(blank=True,upload_to='uploadedimages/')

	trip 		=models.ForeignKey('Trip',on_delete=models.SET_NULL,null=True,blank=True)
class Trip(models.Model):
	#__str__ shows date, {dump: Dump Run,pd: x Stop ~Pickup~ Run}
	scheduleddate=models.DateTimeField() 
	driver		=models.CharField(max_length=100)

	TRIPTYPE_CHOICES=(
		('PD','Pickup/Dropoff'),
		('DMP','Dump Run'))

	triptype 	=models.CharField(max_length=3,choices=TRIPTYPE_CHOICES,default='PD')



class Page(models.Model):
	headerimg=models.ImageField(upload_to='headerimages/')#option to have all names equal/slugged
	tabname=models.CharField(max_length=20,blank=True)
	url=models.CharField(blank=True,max_length=20)
	headertitle=models.CharField(max_length=50)
	headersubtitle=models.CharField(blank=True,max_length=80)

	callstr=models.CharField(blank=True,max_length=25)
	callbtn=models.CharField(blank=True,max_length=25)
	callactn=models.CharField(blank=True,max_length=10)
	def __str__(self):
		return self.url

class Location(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	phone=models.CharField(max_length=15)
	email=models.EmailField(blank=True)
	icon=models.CharField(max_length=10,blank=True)

	volblurb=models.TextField(max_length=1000,blank=True)
	donblurb=models.TextField(max_length=1000,blank=True)
	def __str__(self):
		return self.name
class SocialMedia(models.Model):
	#figures out type from url
	SOC_TYPES=( 
		("IN","Instagram"),
		("FB","Facebook"),
		("TW","Twitter"),
		("YT","YouTube"),
		("SC","SnapChat")
		)
	url=models.URLField()
	order=models.IntegerField()
	soctype=models.CharField(max_length=2,choices=SOC_TYPES)






class Article(models.Model):
	url=models.URLField()
	title=models.CharField(max_length=100,blank=True)
	author=models.CharField(max_length=30)
	paper=models.CharField(max_length=30)
	date=models.DateField()
	img=models.ImageField(blank=True)
	blurb=models.TextField(max_length=1000)
	
	def __str__(self):
		return self.author+', '+self.paper
# class Sale(models.Model):

# 	salecats 	=models.TextField(max_length=50)
# 	saleamt		=models.TextField(max_length=50)#make into flexible types? (x% off, $y off, buy z get $q etc etc etc - match epos?)

# 	saledesc	=models.CharField(max_length=100) #shows in different page or smth? 
# 	salestart	=models.DateTimeField()
# 	saleend		=models.DateTimeField()

