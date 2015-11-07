from django.contrib import admin

from .models import Client  # , Comments


class ClientAdmin(admin.ModelAdmin):

    list_display = ('client_name', 'country', 'was_recent')
    list_filter = ['start_date', 'country']
    fieldsets = [(None, {'fields': ['client_name']}),
                 ('More information', {'fields': ['country',
                                                  'customer_site',
                                                  'state',
                                                  'gas_rate',
                                                  'water_rate'],
                                       'classes': ['collapse']})]

admin.site.register(Client, ClientAdmin)
# admin.site.register(Comments)
