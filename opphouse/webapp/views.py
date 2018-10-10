from django.shortcuts import render
from django.template import RequestContext

from rest_framework import viewsets

from .models import *
from .serializers import *
from .forms import *

import datetime
#render_to_response can include  context_instance=RequestContext(request) for session tracking i think?
locs=Location.objects.all()
#footinvolve has different string per page
#make base info w locations





# Create your views here.
def base(request):
	return render(request,"")
def home(request):
	#needs to include sponsors, major sponsors
	context={
		'page':getpage(request),
		'sponsors':Sponsor.objects.filter(sponsortype='SP'),
		'majorsponsors':Sponsor.objects.filter(sponsortype='MJ'),
		'locations':locs
	}
	return render(request,"webapp/about.html",context)


def events(request):

	path=request.get_full_path()
	evlist=Event.objects.all()#gets all events from database, will filter out past ones
	context={
		'events':evlist,
		'page':getpage(request),
		'locations':locs
	}

	print(context)
	return render(request,"webapp/events.html",context)

def contact(request):
	path=request.get_full_path()
	context={
		'form':ContactForm(request.POST),
		'page':getpage(request),
		'locations':locs
	}
	return render(request,"webapp/contact.html",context)

def donate(request):
	#CHECK IF DOCK OPEN
	path=request.get_full_path()
	context={'page':getpage(request),
		'locations':locs
	}
	return render(request,"webapp/donate.html",context)
	

def thriftstore(request):
	path=request.get_full_path()
	#excluded items?
	
	context={'page':getpage(request),
	'dock':dockcheck(),
	'articles':Article.objects.all(),
	'locations':locs
	}
	return render(request,"webapp/thrift-store.html",context)



def wheelsforhope(request):
	path=request.get_full_path()
	form=CarForm(request.POST)
	dform=DonorForm(request.POST)
	context={
	"form":form,
	'dform':dform,
	'page':getpage(request),
		'locations':locs
	}
	return render(request,"webapp/wheels-for-hope.html",context)




def volunteer(request):
	path=request.get_full_path()
	context={'page':getpage(request),
		'locations':locs}
	print(context)
	return render(request,"webapp/volunteer.html",context)

def truckscheduler(request):
	stops={0:'testing',1:'tested',2:'testocracy'}
	maxpertrip=6
	pertrip=3
	trips=1
	context={'stops':stops,
	'num':['']*5,
	'page':getpage(request),
		'locations':locs
	}#janky
	return render(request,"webapp/truckscheduler.html",context)



class DockViewSet(viewsets.ModelViewSet):
	queryset=Dock.objects.all()
	serializer_class = DockSerializer


class PickupViewSet(viewsets.ModelViewSet):
	queryset=Pickup.objects.all()
	serializer_class = PickupSerializer