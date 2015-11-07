from django.db import models
from django.utils import timezone
import arrow
import datetime
import ISO3166

ISO3166_CHOICES = ISO3166.ISO3166


class Client(models.Model):
    start_date = models.DateTimeField('Registered Date')
    owner = models.ForeignKey('auth.User', related_name='client')

    client_name = models.CharField('Client', default='', max_length=256)
    account_name = models.CharField('Account Name', default='', max_length=256)
    project_name = models.CharField('Project Name', default='', max_length=256)

    address = models.TextField('Address', max_length=750, default='')
    city = models.CharField('City', max_length=256, default='')
    state = models.CharField('State', max_length=128, default='')
    country = models.CharField(max_length=2, default='US', choices=ISO3166_CHOICES)

    electric_rate = models.FloatField('Electric Rate ($/kWh)', default=0)
    gas_rate = models.FloatField('Gas Rate ($/Therms)', default=0)
    water_rate = models.FloatField('Water Rate ($/Gallons)', default=0)
    sewer_rate = models.FloatField('Sewer Rate ($/Gallons)', default=0)

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

# class Comments(models.Model):
# 	comment = models.TextField('Comments', max_length=500)
