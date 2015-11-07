from django.shortcuts import render

from boiler_blowdown.models import BoilerBlowdown
from boiler_blowdown.serializers import BoilerBlowdownSerializer

from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import filters, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters

# Boiler Blowdown Filter
class BoilerBlowdownFilter(django_filters.FilterSet):
    class Meta:
        model = BoilerBlowdown
        fields = ['client']


# Create your views here.
class BoilerBlowdownViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = BoilerBlowdownFilter
        queryset = BoilerBlowdown.objects.all()
        serializer_class = BoilerBlowdownSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
