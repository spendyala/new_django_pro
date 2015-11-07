from django.contrib import admin

# Register your models here.
from .models import StackedEconomizer  # , Comments


class StackedEconomizerAdmin(admin.ModelAdmin):

    list_display = ('boiler_stacked_economizer', 'client', 'was_recent')
    list_filter = ['client']
    fieldsets = [('None', {'fields': ['client',
                                      'start_date',
                                      'boiler_stacked_economizer',
                                      'gas_rate',
                                      'hours_of_operations',
                                      'boiler_size_hp',
                                      'initial_stack_gas_temp_f',
                                      'average_fire_rate']})]

admin.site.register(StackedEconomizer, StackedEconomizerAdmin)
