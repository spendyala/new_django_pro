from rest_framework import serializers
from pipe_insulation.models import PipeInsulation
from django.contrib.auth.models import User

class PipeInsulationSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = PipeInsulation
        fields = ('id', 'url', 'client', 'start_date', 'owner', 'notes',
                  'name', 'length_of_pipe', 'nps_pipe_size_inches',
                  'working_fluid', 'process_temp_or_pressure',
                  'system_efficiency', 'ambient_temp', 'system_hours_per_year',
                  'wind_speed_mph', 'location', 'base_metal', 'insulation',
                  'insulation_thickness', 'jacket_material')
