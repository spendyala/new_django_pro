from django.shortcuts import render

from chiller.models import Chiller, ChillerLoopPump, CondensatePump
from chiller.serializers import ChillerSerializer

from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import filters, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters

# Boiler Blowdown Filter
class ChillerFilter(django_filters.FilterSet):
    class Meta:
        model = Chiller
        fields = ['client']


# Create your views here.
class ChillerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ChillerFilter
    queryset = Chiller.objects.all()
    serializer_class = ChillerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
