from django.shortcuts import render
from clients.models import Client
from clients.serializers import ClientSerializer, UserSerializer
from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
		"""
		This viewset automatically provides `list`, `create`, `retrieve`,
		`update` and `destroy` actions.
		"""
		queryset = Client.objects.all()
		serializer_class = ClientSerializer
		# import pdb; pdb.set_trace()

		permission_classes = (permissions.IsAuthenticatedOrReadOnly,
												  IsOwnerOrReadOnly,)

		# @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
		# def highlight(self, request, *args, **kwargs):
		# 		snippet = self.get_object()
		# 		return Response(snippet.highlighted)

		def perform_create(self, serializer):
				serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
		"""
		This viewset automatically provides `list` and `detail` actions.
		"""
		queryset = User.objects.all()
		serializer_class = UserSerializer
