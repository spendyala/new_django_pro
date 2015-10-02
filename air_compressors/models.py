from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client


class StackedEconomizer(models.Model):
	start_date = models.DateTimeField('Registered Date')
	client = models.ForeignKey(Client)
	air_compressor = models.CharField('Air Compressor',
									  default='',
									  max_length=128)
	customer_name = models.CharField('Customer Name',
									 default='',
									 max_length=128)
	customer_site = models.CharField('Customer Site',
									  default='',
									  max_length=128)
	project_name = models.CharField('Project Name,
									 default='',
									 max_length=128)
	electric_utility_rate = models.FloatField('Electric Utility Rate (per kWh)',
											  default=0)
	hours_of_operations = models.FloatField('Hours of Operation', default=8760)
	boiler_size_hp = models.FloatField('Boiler Size (HP)',
										 default=1000)
	initial_stack_gas_temp_f = models.FloatField('Initial Stack Gas Temp (F)',
									   default=500)
	average_fire_rate = models.FloatField('Average Fire Rate', default=0)
	owner = models.ForeignKey('auth.User', related_name='stacked_economizer')

	def get_boiler_size_mmbtu_per_hr(self):
		return round(self.boiler_size_hp *
					 0.0334714, 3)

	def get_recoverable_heat_mmbtu_per_hr(self):
		return round(
			self.get_boiler_size_mmbtu_per_hr() *
			(pow(self.initial_stack_gas_temp_f, 2.3)/ 18500000.0) *
			self.average_fire_rate / 100.0, 3)

	def get_recoverable_heat_therms_per_year(self):
		return round(
			self.get_recoverable_heat_mmbtu_per_hr() * 10.0 *
			self.hours_of_operations, 3)

	def get_savings(self):
		return round(
			self.get_recoverable_heat_therms_per_year() * self.gas_rate, 3)

	def was_recent(self):
		return self.start_date >= timezone.now() - datetime.timedelta(days=1)
	was_recent.admin_order_field = 'start_date'
	was_recent.boolean = True
	was_recent.short_description = 'Recently Joined?'

	def __str__(self):
		return self.boiler_stacked_economizer

	def save(self, *args, **kwargs):
		# TODO: add owner
		self.start_date = datetime.datetime.utcnow()
		super(StackedEconomizer, self).save(*args, **kwargs)

	class Meta:
		ordering = ('boiler_stacked_economizer',)
