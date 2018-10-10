
from django.contrib import admin
from .models import *

#Model Admins
class EventAdmin(admin.ModelAdmin):
	list_display=('eventname','startdate')


class SponsorAdmin(admin.ModelAdmin):
	list_display=('sponsorname','sponsortype')
	list_filter=('sponsortype',)

#Model Registration - what models are accessible from admin page
admin.site.register(Event,EventAdmin)
admin.site.register(Donor)
admin.site.register(Sponsor,SponsorAdmin)
admin.site.register(Pickup)
admin.site.register(Car)
admin.site.register(WebPage)
admin.site.register(Location)
admin.site.register(Article)

admin.site.register(Dock)
admin.site.register(Trip)


