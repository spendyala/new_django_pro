from rest_framework import serializers
from air_compressors.models import AirCompressor
from django.contrib.auth.models import User

class AirCompressorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    get_hourly_kwh_consumed = serializers.ReadOnlyField()
    get_hourly_cost_of_operation = serializers.ReadOnlyField()
    get_annual_cost_of_operation = serializers.ReadOnlyField()
    get_reduced_line_pressure_from = serializers.ReadOnlyField()
    get_proposed_pressure_decrease = serializers.ReadOnlyField()
    get_estimated_ann_savings_per_2_psi_reduction = serializers.ReadOnlyField()
    get_annual_cost_before_psi_setback = serializers.ReadOnlyField()
    get_annual_cost_after_psi_setback = serializers.ReadOnlyField()
    get_annual_savings_after_psi_setback = serializers.ReadOnlyField()
    get_estimated_air_leak_25_percent_of_costs = serializers.ReadOnlyField()
    get_estimated_air_leak_40_percent_of_costs = serializers.ReadOnlyField()

    class Meta:
        model = AirCompressor
        fields = ('id', 'url', 'client', 'start_date',
                  'air_compressor', 'customer_name',
                  'customer_site', 'owner', 'project_name',
                  'compressor_name', 'notes',
                  'manufacturer', 'model_info', 'serial_info',
                  'compressor_type',
                  'vfd_speed_control', 'nameplate_horsepower',
                  'nameplate_max_flow', 'measured_actual_flow',
                  'measured_line_pressure', 'annual_hours_of_operation',
                  'reduce_line_pressure_to', 'vfd_90_t_fitting',
                  'get_hourly_kwh_consumed', 'get_hourly_cost_of_operation',
                  'get_annual_cost_of_operation',
                  'get_reduced_line_pressure_from',
                  'get_proposed_pressure_decrease',
                  'get_estimated_ann_savings_per_2_psi_reduction',
                  'get_annual_cost_before_psi_setback',
                  'get_annual_cost_after_psi_setback',
                  'get_annual_savings_after_psi_setback',
                  'get_estimated_air_leak_25_percent_of_costs',
                  'get_estimated_air_leak_40_percent_of_costs')
