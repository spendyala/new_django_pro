from django.contrib import admin

# Register your models here.
from .models import (LaborVFDMotor,
                     MaterialsVFDMotor,
                     VfdMotorSetpointSelections,
                     VfdMotorDataPerMonth,
                     VfdMotor)
admin.site.register(VfdMotor)
admin.site.register(LaborVFDMotor)
admin.site.register(MaterialsVFDMotor)
admin.site.register(VfdMotorSetpointSelections)
admin.site.register(VfdMotorDataPerMonth)
