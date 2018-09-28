from django.contrib import admin
from .models import Event, Sponsor

#Model Registration
admin.site.register(Event)
admin.site.register(Sponsor)



#Other
admin.site.site_header="Opportunity House Website Administration"