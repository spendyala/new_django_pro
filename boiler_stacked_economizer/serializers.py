from rest_framework import serializers
from boiler_stacked_economizer.models import BoilerStackedEconomizer
from django.contrib.auth.models import User

class BoilerStackedEconomizerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    get_boiler_size_mmbtu_per_hr = serializers.ReadOnlyField()
    get_recoverable_heat_mmbtu_per_hr = serializers.ReadOnlyField()
    get_recoverable_heat_therms_per_yr = serializers.ReadOnlyField()
    get_savings = serializers.ReadOnlyField()

    class Meta:
        model = BoilerStackedEconomizer
        fields = ('id', 'url', 'client', 'start_date', 'owner',
                  'name', 'boiler_size_hr', 'initial_stack_gas_temp_f',
                  'avg_fire_rate', 'hours_of_operation',
                  'get_boiler_size_mmbtu_per_hr', 'get_savings',
                  'get_recoverable_heat_mmbtu_per_hr',
                  'get_recoverable_heat_therms_per_yr')
