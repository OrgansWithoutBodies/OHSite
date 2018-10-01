from django.contrib import admin
from .models import *

#Model Admins
class EventAdmin(admin.ModelAdmin):
	list_display=('eventname','startdate')


#Model Registration
admin.site.register(Event,EventAdmin)
admin.site.register(Donor)
admin.site.register(Sponsor)
admin.site.register(Pickup)
admin.site.register(Car)


admin.site.register(Trip)


