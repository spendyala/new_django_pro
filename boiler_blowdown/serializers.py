from rest_framework import serializers
from boiler_blowdown.models import BoilerBlowdown
from django.contrib.auth.models import User


class BoilerBlowdownSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    # Existing
    get_existing_annual_quantity_gals = serializers.ReadOnlyField()
    get_existing_annual_quantity_lbs = serializers.ReadOnlyField()
    get_existing_blowdown_energy_loss_btuh = serializers.ReadOnlyField()
    get_existing_blowdown_energy_loss_therms = serializers.ReadOnlyField()
    get_existing_blowdown_energy_recovery_therms = serializers.ReadOnlyField()
    get_existing_blowdown_gallons_per_day = serializers.ReadOnlyField()
    get_existing_energy_loss_therm = serializers.ReadOnlyField()
    get_existing_gas_and_water_cost = serializers.ReadOnlyField()
    get_existing_makeup_water_cost = serializers.ReadOnlyField()
    get_existing_makeup_water_quantity = serializers.ReadOnlyField()
    get_existing_overflow_cost = serializers.ReadOnlyField()
    get_existing_total = serializers.ReadOnlyField()

    # Proposed
    get_proposed_annual_quantity_gals = serializers.ReadOnlyField()
    get_proposed_annual_quantity_lbs = serializers.ReadOnlyField()
    get_proposed_blowdown_energy_loss_btuh = serializers.ReadOnlyField()
    get_proposed_blowdown_energy_loss_therms = serializers.ReadOnlyField()
    get_proposed_blowdown_energy_recovery_therms = serializers.ReadOnlyField()
    get_proposed_blowdown_gallons_per_day = serializers.ReadOnlyField()
    get_proposed_energy_loss_therm = serializers.ReadOnlyField()
    get_proposed_gas_and_water_cost = serializers.ReadOnlyField()
    get_proposed_makeup_water_cost = serializers.ReadOnlyField()
    get_proposed_makeup_water_quantity = serializers.ReadOnlyField()
    get_proposed_overflow_cost = serializers.ReadOnlyField()
    get_proposed_total = serializers.ReadOnlyField()

    # Savings
    get_savings_gas = serializers.ReadOnlyField()
    get_savings_gas_and_water = serializers.ReadOnlyField()
    get_savings_total = serializers.ReadOnlyField()
    get_savings_water = serializers.ReadOnlyField()

    class Meta:
        model = BoilerBlowdown
        fields = ('id',
                  'url',
                  'owner',
                  'start_date',
                  'notes',
                  'client',
                  'boiler_blowdown_name',
                  'makeup_water_temperature',

                  # Existing Inputs
                  'existing_blowdown_duration_mins',
                  'existing_blowdown_frequency_per_day',
                  'existing_blowdown_rate_gpm',
                  'existing_days_of_operation',
                  'existing_discharge_temp_in_f',
                  'existing_heat_recovery_efficiency_perc',

                  # Proposed Inputs
                  'proposed_blowdown_duration_mins',
                  'proposed_blowdown_frequency_per_day',
                  'proposed_blowdown_rate_gpm',
                  'proposed_days_of_operation',
                  'proposed_discharge_temp_in_f',
                  'proposed_heat_recovery_efficiency_perc',

                  # Existing Values
                  'get_existing_annual_quantity_gals',
                  'get_existing_annual_quantity_lbs',
                  'get_existing_blowdown_energy_loss_btuh',
                  'get_existing_blowdown_energy_loss_therms',
                  'get_existing_blowdown_energy_recovery_therms',
                  'get_existing_blowdown_gallons_per_day',
                  'get_existing_energy_loss_therm',
                  'get_existing_gas_and_water_cost',
                  'get_existing_makeup_water_cost',
                  'get_existing_makeup_water_quantity',
                  'get_existing_overflow_cost',
                  'get_existing_total',

                  # Proposed Values
                  'get_proposed_annual_quantity_gals',
                  'get_proposed_annual_quantity_lbs',
                  'get_proposed_blowdown_energy_loss_btuh',
                  'get_proposed_blowdown_energy_loss_therms',
                  'get_proposed_blowdown_energy_recovery_therms',
                  'get_proposed_blowdown_gallons_per_day',
                  'get_proposed_energy_loss_therm',
                  'get_proposed_gas_and_water_cost',
                  'get_proposed_makeup_water_cost',
                  'get_proposed_makeup_water_quantity',
                  'get_proposed_overflow_cost',
                  'get_proposed_total',
                  # Savings Values
                  'get_savings_gas',
                  'get_savings_gas_and_water',
                  'get_savings_total',
                  'get_savings_water',)
