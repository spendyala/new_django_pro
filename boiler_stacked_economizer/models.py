from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client


class BoilerStackedEconomizer(models.Model):
    client = models.ForeignKey(Client)
    start_date = models.DateTimeField('Registered Date')
    name = models.CharField('Boiler Stacked Economizer Name',
                            default='',
                            max_length=128)
    boiler_size_hr = models.FloatField('Boiler Size (HP)',
                                       default=0)
    initial_stack_gas_temp_f = models.FloatField('Initial Stack Gas Temp (F)',
                                                 default=0)
    avg_fire_rate = models.FloatField('Average Fire Rate',
                                      default=0)
    hours_of_operation = models.FloatField('Hours of Operation',
                                           default=0)

    owner = models.ForeignKey('auth.User',
                              related_name='boiler_stacked_economizer')

    def get_boiler_size_mmbtu_per_hr(self):
        return (self.boiler_size_hr * 0.0334714)

    def get_recoverable_heat_mmbtu_per_hr(self):
        return (self.get_boiler_size_mmbtu_per_hr() *
                (pow(self.initial_stack_gas_temp_f, 2.3)/18500000.0) *
                (self.avg_fire_rate/100.0))

    def get_recoverable_heat_therms_per_yr(self):
        return (self.get_recoverable_heat_mmbtu_per_hr() * 10 *
                self.hours_of_operation)

    def get_savings(self):
        return (self.get_recoverable_heat_therms_per_yr() *
                self.client.gas_rate)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # TODO: add owner
        self.start_date = datetime.datetime.utcnow()
        super(BoilerStackedEconomizer, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
