from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client
from supporting_files import read_steam_trap


STEAM_TRAP_DATA = read_steam_trap.get_steam_trap_data()
TRAP_SIZE_DATA = read_steam_trap.get_trap_size_data()

STEAM_TRAP_CHOICES = {x:STEAM_TRAP_DATA[x].get('latent_btu_per_lb')
                      for x in STEAM_TRAP_DATA}
TRAP_SIZE_CHOICES = {x:TRAP_SIZE_DATA[x].get('trap_orifice_size')
                     for x in TRAP_SIZE_DATA}


class SteamTrap(models.Model):
    client = models.ForeignKey(Client)
    start_date = models.DateTimeField('Registered Date')
    steam_trap_number = models.CharField('Failed Trap #', default='',
                                         max_length=127)
    hours_of_operation = models.IntegerField('Hours of Operation', default=8760)
    boiler_efficiency = models.FloatField('Boiler Efficiency %', default=80.0)
    location_description = models.CharField('Location/Description', default='',
                                            max_length=255)
    pressure_in_psig = models.FloatField('Pressure (psig)',
                                         default=100)
    trap_pipe_size = models.FloatField('Trap Pipe Size (inch)',
                                       default=0.5)
    notes = models.TextField('Notes', default='')
    owner = models.ForeignKey('auth.User', related_name='steam_trap')

    def get_therm_rate(self):
        return self.client.gas_rate

    def get_steam_energy_btu_per_lb(self):
        return STEAM_TRAP_CHOICES[self.pressure_in_psig]

    def get_steam_loss_pph(self):
        return round(24.24 * self.absolute_pressure_psia() *
                     pow(TRAP_SIZE_CHOICES[self.trap_pipe_size], 2), 2)

    def get_gas_usage_therms_per_hour(self):
        return round(float(self.get_steam_loss_pph() *
                     self.get_steam_energy_btu_per_lb() *
                     (1.0/self.boiler_efficiency) *
                     10 * (1.0/10000.0)), 3)

    def absolute_pressure_psia(self):
        if self.pressure_in_psig:
            return round(self.pressure_in_psig + 14.696, 3)
        else:
            return 0

    def size_trap_orifice(self):
        return TRAP_SIZE_CHOICES[self.trap_pipe_size]

    def get_cost_per_hour(self):
        return round(float(self.get_gas_usage_therms_per_hour() *
                     self.client.gas_rate), 2)

    def get_cost_per_year(self):
        return round(float(self.hours_of_operation *
                     self.get_cost_per_hour()), 2)

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
