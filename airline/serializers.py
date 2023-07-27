from rest_framework import serializers
from .models import Airline

from aircraft.serializers import AircraftSerializer

class AirlineSerializer(serializers.ModelSerializer):

    id = serializers.CharField(source='name', read_only=True)
    aircraft_set = AircraftSerializer(many=True, read_only=True)

    class Meta:
        model = Airline
        fields = '__all__'
        