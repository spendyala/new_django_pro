from rest_framework import serializers
from air_leak.models import AirLeak
from django.contrib.auth.models import User

class AirLeakSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    get_convert_db_to_cmf = serializers.ReadOnlyField()
    get_annual_cost_of_leak = serializers.ReadOnlyField()

    class Meta:
        model = AirLeak
        fields = ('id', 'url', 'client', 'start_date', 'notes',
                  'air_leak', 'owner', 'project_name',
                  'leak_tag_number', 'datetime_time_leak_found',
                  'leak_area_description', 'leak_equipment_desc', 'leak_type',
                  'annual_hours_of_operation', 'leak_db_reading',
                  'leak_reparied_flag', 'get_convert_db_to_cmf',
                  'get_annual_cost_of_leak')
