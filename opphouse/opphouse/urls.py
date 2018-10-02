"""opphouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,include

from rest_framework import routers

from webapp import views

router=routers.DefaultRouter()
router.register(r'pickups',views.PickupViewSet)


urlpatterns = [
    path('api/',include(router.urls)),
	path('',views.home),
    path('truckscheduler/',views.truckscheduler,name='truckscheduler'),
    path('admin/', admin.site.urls,name='adminpage'),
    path('home/',views.home,name='homepage'),
    path('donate/',views.donate,name='donate'),
    path('thrift-store/',views.thriftstore,name='thrift-store'),
    path('volunteer/',views.volunteer,name='volunteer'),
    path('wheels-for-hope/',views.wheelsforhope,name='wheels-for-hope'),
    path('contact/',views.contact,name='contact'),
    path('events/',views.events,name='events'),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]

#make specific urls.py for APIs?

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
