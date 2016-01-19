from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client


class StackedEconomizer(models.Model):
    client = models.ForeignKey(Client)
    boiler_stacked_economizer = models.CharField('Stacked Economizer',
                                                 default='',
                                                 max_length=128)
    start_date = models.DateTimeField('Registered Date')
    # client.gas_rate = models.FloatField('Gas Rate', default=0.5)
    hours_of_operations = models.FloatField('Hours of Operation', default=8760)
    boiler_size_hp = models.FloatField('Boiler Size (HP)',
                                       default=1000)
    initial_stack_gas_temp_f = models.FloatField('Initial Stack Gas Temp (F)',
                                                 default=500)
    average_fire_rate = models.FloatField('Average Fire Rate', default=0)
    notes = models.TextField('Notes', default='')
    owner = models.ForeignKey('auth.User', related_name='stacked_economizer')

    def get_boiler_size_mmbtu_per_hr(self):
        return round(self.boiler_size_hp * 0.0334714, 3)

    def get_recoverable_heat_mmbtu_per_hr(self):
        return round(self.get_boiler_size_mmbtu_per_hr() *
                     round((pow(self.initial_stack_gas_temp_f,
                                2.3) / 18500000.0) *
                     self.average_fire_rate, 2) / 100.0, 3)

    def get_recoverable_heat_therms_per_year(self):
        return round(
            self.get_recoverable_heat_mmbtu_per_hr() * 10.0 *
            self.hours_of_operations, 3)

    def get_savings(self):
        return round(
            self.get_recoverable_heat_therms_per_year() * self.client.gas_rate, 3)

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
