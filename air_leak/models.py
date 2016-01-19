from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client

LEAK_DB_CHOICES = [(10, 0.100),
                   (20, 0.159),
                   (30, 0.312),
                   (40, 0.589),
                   (50, 1.118),
                   (60, 2.178),
                   (70, 3.500),
                   (80, 4.000),
                   (90, 5.000),
                   (100, 6.500)]

LEAK_REPAIR_TYPE = [(1, 'YES'),
                    (2, 'NO')]

class AirLeak(models.Model):
    start_date = models.DateTimeField('Registered Date')
    client = models.ForeignKey(Client)
    air_leak = models.CharField('Air Leak',
                                default='',
                                max_length=128)
    project_name = models.CharField('Project Name',
                                    default='',
                                    max_length=128)
    leak_tag_number = models.CharField('Leak Tag Number',
                                       default='',
                                       max_length=128)
    datetime_time_leak_found = models.DateField('Date Leak found',
                                                null=True,
                                                blank=True)
    leak_area_description = models.CharField('Leak Area Description',
                                             default='',
                                             max_length=128)
    leak_equipment_desc = models.CharField('Leak Equipment Description',
                                           default='',
                                           max_length=128)
    leak_type = models.CharField('Leak Type',
                                 default='',
                                 max_length=128)
    annual_hours_of_operation = models.FloatField(
        'Annual Hours of Operation (Hours)',
        default=0)
    leak_db_reading = models.IntegerField('Leak DB Reading',
                                          choices=LEAK_DB_CHOICES,
                                          default=10)
    leak_reparied_flag = models.IntegerField('Leak Repaired?',
                                             choices=LEAK_REPAIR_TYPE,
                                             default=1)
    notes = models.TextField('Notes', default='')
    owner = models.ForeignKey('auth.User', related_name='air_leak')

    def get_convert_db_to_cmf(self):
        db_to_cmf_dict = dict(LEAK_DB_CHOICES)
        return db_to_cmf_dict[self.leak_db_reading]

    def get_annual_cost_of_leak(self):
        return round(((self.get_convert_db_to_cmf()/4.2) * 0.746 *
                     self.annual_hours_of_operation *
                     self.client.electric_rate) / 0.9, 2)

    def __str__(self):
        return self.air_leak

    def save(self, *args, **kwargs):
        # TODO: add owner
        self.start_date = datetime.datetime.utcnow()
        super(AirLeak, self).save(*args, **kwargs)

    class Meta:
        ordering = ('air_leak',)
