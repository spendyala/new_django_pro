from django.contrib import admin

# Register your models here.
from .models import SteamLeak  # , Comments


class SteamLeakAdmin(admin.ModelAdmin):

    list_display = ('steam_leak_number', 'boiler_efficiency', 'was_recent')
    list_filter = ['client']
    fieldsets = [('None', {'fields': ['client',
                                      'start_date',
                                      'steam_leak_number',
                                      'location_description',
                                      'pressure_in_psig',
                                      'size_leak_in_inch',
                                      'hours_of_operation',
                                      'boiler_efficiency',
                                      'therm_rate']})]

admin.site.register(SteamLeak, SteamLeakAdmin)
