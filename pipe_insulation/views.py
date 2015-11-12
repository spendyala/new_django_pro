from django.shortcuts import render
from pipe_insulation.models import PipeInsulation
from pipe_insulation.serializers import PipeInsulationSerializer
# from clients.serializers import UserSerializer
from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import filters, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters

class PipeInsulationFilter(django_filters.FilterSet):
    class Meta:
        model = PipeInsulation
        fields = ['client']

# Create your views here.
class PipeInsulationViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = PipeInsulationFilter
        queryset = PipeInsulation.objects.all()
        serializer_class = PipeInsulationSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
