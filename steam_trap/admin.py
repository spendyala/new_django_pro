from django.contrib import admin

# Register your models here.
from .models import SteamTrap  # , Comments


class SteamTrapAdmin(admin.ModelAdmin):

    list_display = ('steam_trap_number', 'boiler_efficiency', 'was_recent')
    list_filter = ['client']
    fieldsets = [('None', {'fields': ['client',
                                      'start_date',
                                      'steam_trap_number',
                                      'hours_of_operation',
                                      'boiler_efficiency',
                                      'location_description',
                                      'pressure_in_psig',
                                      'trap_pipe_size']})]
    # fieldsets = [(None, {'fields': ['client_name']}),
    # 			 ('More information', {'fields': ['country', 'customer_site'],
    # 								   'classes': ['collapse']})]

admin.site.register(SteamTrap, SteamTrapAdmin)
