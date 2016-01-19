from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client

CHOICES_YES_NO = [(1, 'YES'),
                  (2, 'NO')]


class BoilerDatacollection(models.Model):
    client = models.ForeignKey(Client)
    start_date = models.DateTimeField('Registered Date')
    owner = models.ForeignKey('auth.User',
                              related_name='boiler_datacollection')

    name = models.CharField('Boiler Data Collection Name',
                            default='',
                            max_length=128)
    boiler_capacity_mbh = models.FloatField('Boiler capacity (MBH)',
                                            default=0)
    hours_of_operation = models.FloatField('Yearly Hours of Operation',
                                           default=8760)
    separately_meter = models.IntegerField('Separately Meter',
                                           choices=CHOICES_YES_NO,
                                           default=0)
    make_up_water_log_separate_bill = models.IntegerField(
        'Make Up Water Log/ Separate Bill',
        choices=CHOICES_YES_NO,
        default=0)
    no_of_steam_traps = models.IntegerField('Number of Steam Traps',
                                            default=0)
    steam_trap_audit_performed = models.DateField(
        'Date Last Steam Trap Audit Performed',
        null=True,
        blank=True)
    is_the_header_insulated = models.IntegerField(
        'Is the Header Insulated',
        choices=CHOICES_YES_NO,
        default=0)
    percentage_condensate_that_returns_to_boiler = models.FloatField(
        'Percent of Condensate that returns to Boiler',
        default=0)
    aerator_tank_temp = models.FloatField(
        'Aerator Tank Temperature',
        default=0,
        help_text='small tank near boiler')
    aerator_tank_pressure = models.FloatField(
        'Aerator Tank Pressure',
        default=80,
        help_text='small tank near boiler')
    production_pressure = models.CharField(
        'Production Pressure',
        default='',
        max_length=128,
        help_text='There could be multiple pressures')
    notes = models.TextField('Notes', default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # TODO: add owner
        self.start_date = datetime.datetime.utcnow()
        super(BoilerDatacollection, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
