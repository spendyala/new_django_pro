from rest_framework import serializers
from boiler_datacollection.models import BoilerDatacollection
from django.contrib.auth.models import User

class BoilerDatacollectionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = BoilerDatacollection
        fields = ('id', 'url', 'client', 'start_date', 'owner', 'notes',
                  'name', 'boiler_capacity_mbh', 'hours_of_operation',
                  'separately_meter', 'make_up_water_log_separate_bill',
                  'no_of_steam_traps', 'steam_trap_audit_performed',
                  'is_the_header_insulated', 'aerator_tank_pressure',
                  'percentage_condensate_that_returns_to_boiler',
                  'production_pressure', 'aerator_tank_temp')
