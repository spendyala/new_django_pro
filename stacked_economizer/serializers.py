from rest_framework import serializers
from stacked_economizer.models import StackedEconomizer
from django.contrib.auth.models import User

class StackedEconomizerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    get_boiler_size_mmbtu_per_hr = serializers.ReadOnlyField()
    get_recoverable_heat_mmbtu_per_hr = serializers.ReadOnlyField()
    get_recoverable_heat_therms_per_year = serializers.ReadOnlyField()
    get_savings = serializers.ReadOnlyField()

    class Meta:
        model = StackedEconomizer
        fields = ('id', 'url', 'client', 'start_date', 'notes',
                  'boiler_stacked_economizer',
                  'hours_of_operations', 'owner', 'boiler_size_hp',
                  'initial_stack_gas_temp_f', 'average_fire_rate',
                  'get_boiler_size_mmbtu_per_hr', 'get_savings',
                  'get_recoverable_heat_mmbtu_per_hr',
                  'get_recoverable_heat_therms_per_year')
