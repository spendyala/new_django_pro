from django.shortcuts import render
from air_compressors.models import AirCompressor
from air_compressors.serializers import AirCompressorSerializer
# from clients.serializers import UserSerializer
from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
class AirCompressorViewSet(viewsets.ModelViewSet):
		"""
		This viewset automatically provides `list`, `create`, `retrieve`,
		`update` and `destroy` actions.
		"""
		queryset = AirCompressor.objects.all()
		serializer_class = AirCompressorSerializer
		permission_classes = (permissions.IsAuthenticatedOrReadOnly,
												  IsOwnerOrReadOnly)

		def perform_create(self, serializer):
			serializer.save(owner=self.request.user)
