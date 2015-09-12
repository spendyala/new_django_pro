from django.contrib import admin

from .models import Client  # , Comments

class ClientAdmin(admin.ModelAdmin):
	# fields = ['client_name', 'country', 'start_date']
	list_filter = ['start_date', 'country']
	list_display = ('client_name', 'country', 'start_date', 'was_recent')
	fieldsets = [
		(None,               {'fields': ['client_name']}),
		('More information', {'fields': ['country', 'customer_site', 'start_date'],
							  'classes': ['collapse']}),
	]

admin.site.register(Client, ClientAdmin)
# admin.site.register(Comments)
