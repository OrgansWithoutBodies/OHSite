from django.shortcuts import render
from django.template import RequestContext

from rest_framework import viewsets

from .models import *
from .serializers import *
from .forms import *
#render_to_response can include  context_instance=RequestContext(request) for session tracking i think?
objs=[{'str':'testing','test':'ing'},
{'str':'tested','othkey':'test'}]

# Create your views here.
def base(request):
	return render(request,"",con)
def home(request):
	context={
		'events':objs,
		'title':'titletext',
		'testlist':['0','1','3']
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
	return render(request,"webapp/contact.html")

def thriftstore(request):
	return render(request,"webapp/thrift-store.html")

def wheelsforhope(request):
	form=CarForm(request.POST)
	dform=DonorForm(request.POST)
	context={
	"form":form,
	'dform':dform
	}
	return render(request,"webapp/wheels-for-hope.html",context)

def volunteer(request):
	return render(request,"webapp/volunteer.html")

def truckscheduler(request):
	pertrip=3
	trips=1
	context={'stops':['test']*pertrip*trips}
	return render(request,"webapp/truckscheduler.html",context)


class PickupViewSet(viewsets.ModelViewSet):
	queryset=Pickup.objects.all()
	serializer_class = PickupSerializer