from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
#WAGTAIL (CMS) stuff 
from wagtail.core.models import Page
from wagtail.core.fields import *
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.utils.decorators import cached_classmethod
#choosers
from wagtail.admin.edit_handlers import FieldPanel,TabbedInterface, ObjectList,StreamFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
#registration
from wagtail.snippets.models import register_snippet

from .blocks import * #import all custom blocks

import datetime
import os
#FUNCTIONS - Views loads from here so its not recursive
def getpage(request): # redundant w Wagtail?  - phase out maybe
	path=request.get_full_path()

	spath=path.split('/pages')#temporary fix to make compatible w cms
	if len(spath)>1:#
		path=spath[-1]
		print(path)
	objs=WebPage.objects.filter(url=path)
	print(objs,WebPage.objects.all())
	if len(objs)!=0:
		return objs[0]
	else:
		return None

def dockcheck():#needs to check if within normal closing hours too
	hourdict={'Sunday':[11,14],
	'Monday':[9,16],
	'Tuesday':[9,16],
	'Wednesday':[9,16],
	'Thursday':[9,16],
	'Friday':[9,16],
	'Saturday':[9,16]}
	rn=datetime.datetime.now()
	dockcontext={}
	if (int(rn.strftime('%H'))>=hourdict[rn.strftime('%A')][0] and int(rn.strftime('%H'))<=hourdict[rn.strftime('%A')][1]):#If within open times
		#check if closed for other reasons
		print('closing time')
		dockdb=Dock.objects.last() #make sure ordering stays consistent
		if dockdb.early_closes.day==rn.day:#checks if the last thing posted was today
			dockcontext['status']='closed'
			dockcontext['reason']=reason
			
		else:
			dockcontext['status']='open'
			
	else:
		dockcontext['status']='closed'
		dockcontext['reason']="scheduled"
	return dockcontext


class DockBlock(blocks.StaticBlock):
		admin_text='Dock Status Block - no configuration'
		class Meta:
				icon ='home'
				template='webapp/blocks/dock_block.html'
				label="Dock Status Checker Ribbon"

		def get_context(self, value, parent_context=None):
			context = super().get_context(value, parent_context=parent_context)
			context['dock']=dockcheck()
			#print(context['dock'])
			return context

class SponsorgridBlock(blocks.StructBlock):
	admin_text='Grid of Sponsors'
	sponsor_header_text=blocks.CharBlock(max_length=30,default="Major Sponsors",help_text="Text on top of Sponsor Grid")
	
	class Meta:
		icon='grip'
		template='webapp/blocks/sponsorgrid_block.html'
	def get_context(self, value, parent_context=None):
			context = super().get_context(value, parent_context=parent_context)
			context['majorsponsors']=Sponsor.objects.filter(sponsortype='MJ')
			return context


###WAGTAIL PAGES###
class BasePage(Page):#all other pages inherit these fields
	headerimg=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL)
	tabname=models.CharField(blank=True,max_length=20)
	baseurl=models.CharField(blank=True,max_length=20)
	headertitle=models.CharField(blank=True,max_length=50)
	headersubtitle=models.CharField(blank=True,max_length=80)

	calltoaction=models.ForeignKey('CallToAction',on_delete=models.SET_NULL,null=True,blank=True)#orange bar at bottom

	template='webapp/base.html'#just in case new page tries to be made w/o template set


	page_panels=Page.content_panels+[
		ImageChooserPanel('headerimg',classname="Header Image"),
		FieldPanel('tabname',classname="full"),
		FieldPanel('headertitle',classname="full"),
		FieldPanel('headersubtitle',classname="full"),
		FieldPanel('baseurl',classname="full"),
		SnippetChooserPanel('calltoaction')
		]

	content_panels=[]
	@cached_classmethod#needs this to be able to add custom stuff to custom tabs, otherwise it would just be applied to the base - bascially turns into lambda fn. see  https://stackoverflow.com/questions/41668167/what-is-the-correct-way-to-extend-wagtail-abstract-models-with-extra-fields
	def get_edit_handler(cls):
		edit_handler = TabbedInterface([
			ObjectList(cls.content_panels,heading='Specific Page Content'),
			ObjectList(cls.page_panels,heading='Shared Page Attributes'),
			ObjectList(cls.promote_panels, heading='Promote'),
	        ObjectList(cls.settings_panels, heading='Settings', classname="settings"),
			])
		return edit_handler.bind_to_model(cls)
	class Meta:
		abstract=True #makes inheritable


class DonatePage(BasePage):
	template='webapp/donate.html'
	body=RichTextField(blank=True)
	test=StreamField( [('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('dock_status',DockBlock()),
        ('loc',LocBlock(target_model='webapp.Location')),
        ('sponsor_grid',SponsorgridBlock()),
        ('two_panel',TwoPanelBlock()),
        ('map',MapBlock()),
        ('info',InfoBlock()),
        ('social',SocialBlock())
        ],blank=True)

	
	pagetitle=models.CharField(max_length=50,blank=True)


	content_panels=[FieldPanel('body',classname="full"),
	StreamFieldPanel('test')]
	def get_context(self,request):
		context=super().get_context(request)
		#context['dock']=dockcheck()
		# print(context['page'].test.sponsor_grid.sponsor_header_text)
		return context
class ContactPage(BasePage):
	template='webapp/contact.html'
	body=RichTextField(blank=True)
	content_panels=BasePage.content_panels+[
	]

class ThriftPage(BasePage):
	template='webapp/thrift-store.html'
	

	content_panels=BasePage.content_panels+[
	]

	def get_context(self,request):
		context=super().get_context(request)
		context['dock']=dockcheck()
		context['articles']=Article.objects.all()
		return context


class VolunteerPage(BasePage):
	template='webapp/volunteer.html'

	content_panels=BasePage.content_panels+[
	]

class HomePage(BasePage):
	template='webapp/about.html'

	content_panels=BasePage.content_panels+[
	]

class WheelsforhopePage(BasePage):
	template='webapp/wheels-for-hope.html'

	content_panels=BasePage.content_panels+[
	]

class EventsPage(BasePage):
	template='webapp/events.html'

	content_panels=BasePage.content_panels+[
	]

	def get_context(self,request):
		context=super().get_context(request)
		context['events']=Event.objects.all()
		return context

###DJANGO MODELS - SNIPPETIZED###
@register_snippet
class CallToAction(models.Model):
	callstr=models.CharField(max_length=25)
	callbtn=models.CharField(max_length=25)
	callactn=models.CharField(blank=True,max_length=10)
	class Meta:
		verbose_name_plural="Calls To Action"
	def __str__(self):
		return str(self.callstr)+' - '+str(self.callbtn)

@register_snippet
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

@register_snippet
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

@register_snippet
class Location(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	phone=models.CharField(max_length=15)
	email=models.EmailField(blank=True)
	icon=models.CharField(max_length=10,blank=True)

	volblurb=models.TextField(max_length=1000,blank=True)
	donblurb=models.TextField(max_length=1000,blank=True)

	#hours=models. #have some way of setting hours easily
	def __str__(self):
		return self.name
@register_snippet
class SocialMedia(models.Model):
	#figures out type from url
	#Show_in_header/footer bool
	SOC_TYPES=( 
		("IN","Instagram"),
		("FB","Facebook"),
		("TW","Twitter"),
		("YT","YouTube"),
		("SC","SnapChat")
		)
	url=models.URLField()
	order=models.IntegerField(blank=True)
	soctype=models.CharField(max_length=2,choices=SOC_TYPES)
	class Meta:
		verbose_name_plural="Social Media Profiles"
	def __str__(self):
		return self.soctype+' - '+self.url.split('://')[-1].split('www.')[-1]

@register_snippet
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

@register_snippet
class Icon(models.Model):
	def validatevector(value):
		print(value)
		ext=os.path.splitext(value.name)[1]
		valid_extensions = ['.svg']
		if not ext in valid_extensions:
			raise ValidationError(u'File not supported! Please make sure to upload a vector image (ending with .svg)')
	def cleanvector(value):
		#need to add an <a> tag
		#above <svg> add <?xml-stylesheet type="text/css" href="svg.css" ?> to get to reference external stylesheet
 		#adds <symbol id=name> to refer to internals
 		#eventually make able to compile all svgs into one & load at top to be more flexible
		return value




	name	=models.CharField(max_length=30)
	vector	=models.FileField(upload_to='icons',validators=[validatevector])
	def __str__(self):
		return self.name
# class Sale(models.Model):

# 	salecats 	=models.TextField(max_length=50)
# 	saleamt		=models.TextField(max_length=50)#make into flexible types? (x% off, $y off, buy z get $q etc etc etc - match epos?)

# 	saledesc	=models.CharField(max_length=100) #shows in different page or smth? 
# 	salestart	=models.DateTimeField()
# 	saleend		=models.DateTimeField()

###DJANGO MODELS - NON SNIPPETS### (used largely for utility & forms)
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



class WebPage(models.Model):
	headerimg=models.ImageField(upload_to='headerimages/')#option to have all names equal/slugged
	tabname=models.CharField(max_length=20,blank=True)
	url=models.CharField(blank=True,max_length=20)
	headertitle=models.CharField(max_length=50)
	headersubtitle=models.CharField(blank=True,max_length=80)
	calltoaction=models.ForeignKey('CallToAction',on_delete=models.SET_NULL,null=True,blank=True)
	callstr=models.CharField(blank=True,max_length=25)
	callbtn=models.CharField(blank=True,max_length=25)
	callactn=models.CharField(blank=True,max_length=10)
	def __str__(self):
		return self.url

class Dock(models.Model):
	early_closes	=models.DateTimeField()
	reason			=models.CharField(max_length=30,blank=True)
	
	def __str__(self):
		return self.early_closes.strftime('%D')+' because '+self.reason

class Car(models.Model):
	donor 		=models.ForeignKey('Donor',on_delete=models.CASCADE)
	
	vin			=models.CharField(max_length=17) #autocheck vin?
	mileage		=models.DecimalField(decimal_places=1,max_digits=10)#multiple choice
	
	year		=models.IntegerField()
	make		=models.CharField(max_length=30)
	carmodel	=models.CharField(max_length=30)
	#does it run/have the title needed
	extrainfo	=models.TextField(blank=True)

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
