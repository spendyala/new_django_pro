from django.contrib import admin

# Register your models here.
from pipe_insulation.models import PipeInsulation  # , Comments

admin.site.register(PipeInsulation)
