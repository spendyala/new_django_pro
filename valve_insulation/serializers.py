from rest_framework import serializers
from valve_insulation.models import ValveInsulation
from django.contrib.auth.models import User

class ValveInsulationSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = ValveInsulation
        fields = ('id', 'url', 'client', 'start_date', 'owner', 'notes',
                  'name', 'valve_type', 'quantity', 'nps_pipe_size_inches',
                  'working_fluid', 'process_temp_or_pressure',
                  'system_efficiency', 'ambient_temp', 'system_hours_per_year',
                  'wind_speed_mph', 'location', 'base_metal', 'insulation',
                  'insulation_thickness', 'jacket_material')
