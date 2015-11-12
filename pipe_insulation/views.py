from django.shortcuts import render
from valve_insulation.models import ValveInsulation
from valve_insulation.serializers import ValveInsulationSerializer
# from clients.serializers import UserSerializer
from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import filters, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters

class ValveInsulationFilter(django_filters.FilterSet):
    class Meta:
        model = ValveInsulation
        fields = ['client']

# Create your views here.
class ValveInsulationViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = ValveInsulationFilter
        queryset = ValveInsulation.objects.all()
        serializer_class = ValveInsulationSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
