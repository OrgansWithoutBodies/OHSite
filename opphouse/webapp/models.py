from django.db import models



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

	price		=models.SmallIntegerField()
	img 		=models.ImageField()
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

