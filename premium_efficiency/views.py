from django.shortcuts import render
from premium_efficiency.models import PremiumEfficiency
from premium_efficiency.serializers import PremiumEfficiencySerializer
# from clients.serializers import UserSerializer
from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
class PremiumEfficiencyViewSet(viewsets.ModelViewSet):
		"""
		This viewset automatically provides `list`, `create`, `retrieve`,
		`update` and `destroy` actions.
		"""
		queryset = PremiumEfficiency.objects.all()
		serializer_class = PremiumEfficiencySerializer
		permission_classes = (permissions.IsAuthenticatedOrReadOnly,
												  IsOwnerOrReadOnly)

		def perform_create(self, serializer):
			serializer.save(owner=self.request.user)
