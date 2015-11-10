from django.shortcuts import render
from vfd.models import (LaborVFDMotor,
                        MaterialsVFDMotor,
                        VfdMotorSetpointSelections,
                        VfdMotorDataPerMonth,
                        VfdMotor)
from vfd.serializers import (LaborVFDMotorSerializer,
                             MaterialsVFDMotorSerializer,
                             VfdMotorSetpointSelectionsSerializer,
                             VfdMotorDataPerMonthSerializer,
                             VfdMotorSerializer)
# from clients.serializers import UserSerializer
from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import filters, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters


class VfdMotorFilter(django_filters.FilterSet):
    class Meta:
        model = VfdMotor
        fields = ['client']

# Create your views here.
class VfdMotorViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = VfdMotorFilter
        queryset = VfdMotor.objects.all()
        serializer_class = VfdMotorSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class VfdMotorDataPerMonthFilter(django_filters.FilterSet):
    class Meta:
        model = VfdMotorDataPerMonth
        fields = ['client_vfd']

# Create your views here.
class VfdMotorDataPerMonthViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = VfdMotorDataPerMonthFilter
        queryset = VfdMotorDataPerMonth.objects.all()
        serializer_class = VfdMotorDataPerMonthSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class VfdMotorSetpointSelectionsFilter(django_filters.FilterSet):
    class Meta:
        model = VfdMotorSetpointSelections
        fields = ['client_vfd']

# Create your views here.
class VfdMotorSetpointSelectionsViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = VfdMotorSetpointSelectionsFilter
        queryset = VfdMotorSetpointSelections.objects.all()
        serializer_class = VfdMotorSetpointSelectionsSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class MaterialsVFDMotorFilter(django_filters.FilterSet):
    class Meta:
        model = MaterialsVFDMotor
        fields = ['client_vfd']

# Create your views here.
class MaterialsVFDMotorViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = MaterialsVFDMotorFilter
        queryset = MaterialsVFDMotor.objects.all()
        serializer_class = MaterialsVFDMotorSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                                                  IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class LaborVFDMotorFilter(django_filters.FilterSet):
    class Meta:
        model = LaborVFDMotor
        fields = ['client_vfd']

# Create your views here.
class LaborVFDMotorViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = LaborVFDMotorFilter
        queryset = LaborVFDMotor.objects.all()
        serializer_class = LaborVFDMotorSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                                                  IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
