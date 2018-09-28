from django.contrib import admin
from .models import Event, Sponsor

#Model Admins
class EventAdmin(admin.ModelAdmin):
	list_display=('eventname','startdate')


#Model Registration
admin.site.register(Event,EventAdmin)
admin.site.register(Sponsor)


