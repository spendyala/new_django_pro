from rest_framework import serializers
from steam_trap.models import SteamTrap
from django.contrib.auth.models import User

class SteamTrapSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    get_steam_energy_btu_per_lb = serializers.ReadOnlyField()
    get_steam_loss_pph = serializers.ReadOnlyField()
    get_gas_usage_therms_per_hour = serializers.ReadOnlyField()
    absolute_pressure_psia = serializers.ReadOnlyField()
    size_trap_orifice = serializers.ReadOnlyField()
    get_cost_per_hour = serializers.ReadOnlyField()
    get_cost_per_year = serializers.ReadOnlyField()
    get_therm_rate = serializers.ReadOnlyField()

    class Meta:
        model = SteamTrap
        fields = ('id', 'url', 'client', 'start_date', 'steam_trap_number',
                  'hours_of_operation', 'owner', 'boiler_efficiency', 'notes',
                  'location_description', 'pressure_in_psig', 'trap_pipe_size',
                  'get_steam_energy_btu_per_lb', 'get_steam_loss_pph',
                  'get_gas_usage_therms_per_hour', 'absolute_pressure_psia',
                  'size_trap_orifice', 'get_cost_per_hour',
                  'get_cost_per_year', 'get_therm_rate')
