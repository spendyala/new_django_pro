from rest_framework import serializers
from clients.models import Client, ISO3166_CHOICES
from django.contrib.auth.models import User

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    start_date = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Client
        fields = ('id', 'url', 'start_date', 'owner', 'client_name',
                  'account_name', 'project_name', 'address', 'city', 'state',
                  'country', 'electric_rate', 'gas_rate', 'water_rate',
                  'sewer_rate')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.HyperlinkedRelatedField(many=True,
                                                 view_name='client-detail',
                                                 read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'client')
