from rest_framework import serializers
from steam_leaks.models import SteamLeak
from django.contrib.auth.models import User

class SteamLeakSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    absolute_pressure_psia = serializers.ReadOnlyField()
    get_steam_loss_pph = serializers.ReadOnlyField()
    get_steam_energy_btu_per_lb = serializers.ReadOnlyField()
    get_gas_usage_therms_per_hour = serializers.ReadOnlyField()
    get_cost_per_hour = serializers.ReadOnlyField()
    get_cost_per_year = serializers.ReadOnlyField()
    get_therm_rate = serializers.ReadOnlyField()

    class Meta:
        model = SteamLeak
        fields = ('id', 'url', 'client', 'start_date', 'steam_leak_number',
                  'hours_of_operation', 'owner', 'boiler_efficiency', 'notes',
                  'location_description', 'pressure_in_psig',
                  'size_leak_in_inch', 'absolute_pressure_psia',
                  'get_steam_loss_pph', 'get_steam_energy_btu_per_lb',
                  'get_gas_usage_therms_per_hour', 'get_cost_per_hour',
                  'get_cost_per_year', 'get_therm_rate')
