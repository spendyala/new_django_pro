from django.shortcuts import render
from boiler_stacked_economizer.models import BoilerStackedEconomizer
from boiler_stacked_economizer.serializers import BoilerStackedEconomizerSerializer
# from clients.serializers import UserSerializer
from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import filters, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters

class BoilerStackedEconomizerFilter(django_filters.FilterSet):
    class Meta:
        model = BoilerStackedEconomizer
        fields = ['client']

# Create your views here.
class BoilerStackedEconomizerViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = BoilerStackedEconomizerFilter
        queryset = BoilerStackedEconomizer.objects.all()
        serializer_class = BoilerStackedEconomizerSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
