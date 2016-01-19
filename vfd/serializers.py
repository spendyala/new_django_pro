from rest_framework import serializers
from vfd.models import LaborVFDMotor, MaterialsVFDMotor, VfdMotorSetpointSelections, VfdMotorDataPerMonth, VfdMotor
from django.contrib.auth.models import User

class VfdMotorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    was_recent = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = VfdMotor
        fields = ('id', 'url', 'client', 'start_date', 'notes',
                  'vfd_name', 'motor_horse_pwr', 'owner',
                  'existing_motor_efficiency',
                  'proposed_vfd_efficiency', 'motor_load', 'was_recent')


class VfdMotorDataPerMonthSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    get_existing_kwh = serializers.ReadOnlyField()
    get_existing_cost_of_operation = serializers.ReadOnlyField()
    get_ui_name = serializers.ReadOnlyField()

    class Meta:
        model = VfdMotorDataPerMonth
        fields = ('id', 'url', 'client_vfd', 'start_date', 'month', 'owner',
                  'hours_of_operation', 'get_existing_kwh', 'get_ui_name',
                  'get_existing_cost_of_operation')


class VfdMotorSetpointSelectionsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    get_proposed_kwh = serializers.ReadOnlyField()
    get_proposed_cost_of_operation = serializers.ReadOnlyField()

    class Meta:
        model = VfdMotorSetpointSelections
        fields = ('id', 'url', 'client_vfd', 'start_date', 'owner',
                  'get_proposed_kwh', 'speed_percent', 'percent_of_time',
                  'get_proposed_cost_of_operation')


class MaterialsVFDMotorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    get_extended_cost = serializers.ReadOnlyField()
    get_ges_each_cost = serializers.ReadOnlyField()

    class Meta:
        model = MaterialsVFDMotor
        fields = ('id', 'url', 'client_vfd', 'start_date', 'item', 'supplier',
                  'description', 'ges_cost_each', 'ges_markup', 'quantity',
                  'owner', 'get_extended_cost', 'get_ges_each_cost')

class LaborVFDMotorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    get_customer_price = serializers.ReadOnlyField()

    class Meta:
        model = LaborVFDMotor
        fields = ('id', 'url', 'client_vfd', 'start_date', 'item', 'vendor',
                  'hourly_rate', 'fixed_cost', 'ges_cost', 'ges_markup',
                  'quantity', 'owner', 'get_customer_price')
