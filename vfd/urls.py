from vfd import views

from django.conf.urls import url, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'vfd_motor', views.VfdMotorViewSet)
router.register(r'vfd_motor_data_per_month', views.VfdMotorDataPerMonthViewSet)
router.register(r'vfd_motor_setpoint_selections', views.VfdMotorSetpointSelectionsViewSet)
router.register(r'materials_vfd_motor', views.MaterialsVFDMotorViewSet)
router.register(r'labor_vfd_motor', views.LaborVFDMotorViewSet)

urlpatterns = [
		url(r'^', include(router.urls))
]
