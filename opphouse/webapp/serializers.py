from rest_framework import serializers
from .models import *

class PickupSerializer(serializers.ModelSerializer):
	class Meta:
		model=Pickup
		fields='__all__'
		depth=2 #unpacks associated fields :)
		#read_only_fields=(,)
		