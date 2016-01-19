from rest_framework import serializers
from premium_efficiency.models import PremiumEfficiency
from django.contrib.auth.models import User

class PremiumEfficiencySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    get_existing_energy_cost_full_load = serializers.ReadOnlyField()
    get_proposed_energy_cost_full_load = serializers.ReadOnlyField()
    get_existing_energy_cost_three_fourth_load = serializers.ReadOnlyField()
    get_proposed_energy_cost_three_fourth_load = serializers.ReadOnlyField()
    get_existing_energy_cost_half_load = serializers.ReadOnlyField()
    get_proposed_energy_cost_half_load = serializers.ReadOnlyField()
    get_purchase_price_diff = serializers.ReadOnlyField()
    get_energy_cost_full_load_diff = serializers.ReadOnlyField()
    get_energy_cost_three_fourth_load_diff = serializers.ReadOnlyField()
    get_energy_cost_half_load_diff = serializers.ReadOnlyField()

    class Meta:
        model = PremiumEfficiency
        fields = ('id', 'url', 'client', 'start_date', 'notes',
                  'motor_name', 'annual_operating_hours',
                  'owner', 'motor_nameplate_hp',
                  'existing_full_load_eff', 'existing_three_fourth_load_eff',
                  'existing_half_load_eff', 'existing_motor_purchase_price',
                  'proposed_full_load_eff', 'proposed_three_fourth_load_eff',
                  'proposed_half_load_eff', 'proposed_motor_purchase_price',
                  'motor_nameplate_rpm', 'get_existing_energy_cost_full_load',
                  'get_proposed_energy_cost_full_load',
                  'get_existing_energy_cost_three_fourth_load',
                  'get_proposed_energy_cost_three_fourth_load',
                  'get_existing_energy_cost_half_load',
                  'get_proposed_energy_cost_half_load',
                  'get_purchase_price_diff',
                  'get_energy_cost_full_load_diff',
                  'get_energy_cost_three_fourth_load_diff',
                  'get_energy_cost_half_load_diff')
