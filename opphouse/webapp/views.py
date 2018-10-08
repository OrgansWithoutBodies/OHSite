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
def getpage(request):
	path=request.get_full_path()
	objs=Page.objects.filter(url=path)
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
	if (int(rn.strftime('%H'))>=hourdict[rn.strftime('%A')][0] and int(rn.strftime('%H'))<=hourdict[rn.strftime('%A')][1]):#If within open times
		#check if closed for other reasons
		print('closing time')
		dockdb=Dock.objects.last() #make sure ordering stays consistent
		if dockdb.early_closes.day==rn.day:#checks if blank

			return dockdb.reason 
		else:
			return False #returns "is open" - confusing 
	else:
		return "scheduled"


# Create your views here.
def base(request):
	return render(request,"")
def home(request):
	#needs to include sponsors, major sponsors
	print(dockcheck())
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
	x=dockcheck()
	if x!=False:
		reason=x
		dockstatus='closed'
	else:
		reason=""
		dockstatus='open'
	context={'page':getpage(request),
	'dockstatus':dockstatus,
	'dockreason':reason,
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