from django.contrib import admin

# Register your models here.
from .models import Chiller, ChillerLoopPump, CondensatePump
admin.site.register(Chiller)
admin.site.register(ChillerLoopPump)
admin.site.register(CondensatePump)
