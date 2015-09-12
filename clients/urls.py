from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
from rest_framework import renderers
# from snippets.views import ClientViewSet, UserViewSet
# from django.conf.urls import url, include
from clients import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
		url(r'^', include(router.urls)),
		url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
		url(r'^html_client', )
]
