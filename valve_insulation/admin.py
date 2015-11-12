from django.contrib import admin

# Register your models here.
from valve_insulation.models import ValveInsulation  # , Comments

admin.site.register(ValveInsulation)
