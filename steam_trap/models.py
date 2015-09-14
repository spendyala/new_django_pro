from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client


class SteamTrap(models.Model):
	client = models.ForeignKey(Client)
	start_date = models.DateTimeField('Registered Date')
	hours_of_operation = models.IntegerField('Hours of Operation', default=8760)
	boiler_efficiency = models.FloatField('Boiler Efficiency %', default=80.0)
	steam_trap_number = models.CharField('Failed Trap #', default='',
										 max_length=127)
	location_description = models.CharField('Location/Description', default='',
											max_length=255)
	pressure_in_psig = models.FloatField('Pressure (psig)', default=100)
	owner = models.ForeignKey('auth.User', related_name='steam_trap')

	def absolute_pressure_psia(self):
		if self.pressure_in_psig:
			return round(self.pressure_in_psig + 14.696, 3)
		else:
			return 0

	def was_recent(self):
		return self.start_date >= timezone.now() - datetime.timedelta(days=1)
	was_recent.admin_order_field = 'start_date'
	was_recent.boolean = True
	was_recent.short_description = 'Recently Joined?'

	def __str__(self):
		return self.steam_trap_number

	def save(self, *args, **kwargs):
		# TODO: add owner
		self.start_date = datetime.datetime.utcnow()
		super(SteamTrap, self).save(*args, **kwargs)

	class Meta:
		ordering = ('steam_trap_number',)
