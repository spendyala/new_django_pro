from django.shortcuts import render
from steam_trap.models import SteamTrap
from steam_trap.serializers import SteamTrapSerializer
# from clients.serializers import UserSerializer
from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import filters, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters

class SteamTrapFilter(django_filters.FilterSet):
    class Meta:
        model = SteamTrap
        fields = ['client']

# Create your views here.
class SteamTrapViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = SteamTrapFilter
        queryset = SteamTrap.objects.all()
        serializer_class = SteamTrapSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
