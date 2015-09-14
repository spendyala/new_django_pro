from django.db import models

from django.db import models
from django.utils import timezone
import arrow
import datetime

from clients.models import Client

ISO3166_CHOICES = ISO3166.ISO3166


class SteamTrap(models.Model):
	client = models.ForeignKey(Client)
	start_date = models.DateTimeField('Registered Date')
	hours_of_operation = models.IntegerField('Hours of Operation', default=8760)
	boiler_efficiency = models.FloatField('Boiler Efficiency %', default=80.0)
	steam_trap_number = models.CharField('Failed Trap #', default='')
	location_description = models.CharField('Location/Description', default='')
	pressure_in_psig = mdoels.FloatField('Pressure (psig)', default=100)


	def absolute_pressure_psia(self):
		if self.pressure_in_psig:
			return round(self.pressure_in_psig + 14.696, 3)
		else:
			return 0


	customer_site = models.CharField('Customer Site', max_length=256, default='')
	owner = models.ForeignKey('auth.User', related_name='client')

	def was_recent(self):
		return self.start_date >= timezone.now() - datetime.timedelta(days=1)
	was_recent.admin_order_field = 'start_date'
	was_recent.boolean = True
	was_recent.short_description = 'Recently Joined?'

	def __str__(self):
		return self.client_name

	def save(self, *args, **kwargs):
		# TODO: add owner
		self.start_date = datetime.datetime.utcnow()
		super(Client, self).save(*args, **kwargs)

	class Meta:
		ordering = ('client_name',)
