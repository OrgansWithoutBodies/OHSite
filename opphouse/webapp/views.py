from django.shortcuts import render
from django.template import RequestContext

#render_to_response can include  context_instance=RequestContext(request) for session tracking i think?
objs=[{'str':'testing','test':'ing'},
{'str':'tested','othkey':'test'}]

# Create your views here.
def home(request):
	context={
		'events':objs,
		'title':'titletext',
		'testlist':['0','1','3']
	}
	return render(request,"webapp/about.html",context)


def events(request):
	
	context={
		'events':events
	}
	return render(request,"webapp/events.html",context)

def about(request):
	return render(request,"webapp/about.html")

def contact(request):
	return render(request,"webapp/contact.html")

def thriftstore(request):
	return render(request,"webapp/thrift-store.html")

def wheelsforhope(request):
	return render(request,"webapp/wheels-for-hope.html")

def volunteer(request):
	return render(request,"webapp/volunteer.html")

