from rest_framework import serializers
from .models import timezone,storeTimings,buisenessHour


class storeTimingsSerializer(serializers.ModelSerializer):
    class Meta:
       model=storeTimings
       fields= '__all__'

class timezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model= timezone
        fields= '__all__'

     