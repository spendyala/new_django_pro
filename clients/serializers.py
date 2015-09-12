from rest_framework import serializers
from clients.models import Client, ISO3166_CHOICES
from django.contrib.auth.models import User

class ClientSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Client
		fields = ('url', 'client_name', 'country', 'start_date',
				  'customer_site', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	clients = serializers.HyperlinkedRelatedField(many=True, view_name='client-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'username', 'clients')
