from django.shortcuts import render
from django.template import RequestContext

from rest_framework import viewsets

from .models import *
from .serializers import *
from .forms import *
#render_to_response can include  context_instance=RequestContext(request) for session tracking i think?
objs=[{'str':'testing','test':'ing'},
{'str':'tested','othkey':'test'}]
#footinvolve has different string per page

# Create your views here.
def base(request):
	return render(request,"")
def home(request):
	#needs to include sponsors, major sponsors
	context={
		'events':objs,
		'title':'titletext',
		'sponsors':Sponsor.objects.filter(sponsortype='SP'),
		'majorsponsors':Sponsor.objects.filter(sponsortype='MJ')
	}
	return render(request,"webapp/about.html",context)


def events(request):
	evlist=Event.objects.all()#gets all events from database, will filter out past ones
	context={
		'events':evlist
	}
	return render(request,"webapp/events.html",context)

def about(request):

	return render(request,"webapp/about.html")

def contact(request):
	context={
		'form':ContactForm(request.POST)
	}
	return render(request,"webapp/contact.html",context)

def donate(request):
	context={
	}
	return render(request,"webapp/donate.html",context)
	

def thriftstore(request):
	#excluded items?
	context={

	}
	return render(request,"webapp/thrift-store.html",context)



def wheelsforhope(request):
	form=CarForm(request.POST)
	dform=DonorForm(request.POST)
	context={
	"form":form,
	'dform':dform
	}
	return render(request,"webapp/wheels-for-hope.html",context)




def volunteer(request):
	context={}
	return render(request,"webapp/volunteer.html",context)

def truckscheduler(request):
	pertrip=3
	trips=1
	context={'stops':['test']*pertrip*trips}#janky
	return render(request,"webapp/truckscheduler.html",context)





class PickupViewSet(viewsets.ModelViewSet):
	queryset=Pickup.objects.all()
	serializer_class = PickupSerializer