# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0004_auto_20151013_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoilerDatacollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('name', models.CharField(default=b'', max_length=128, verbose_name=b'Boiler Data Collection Name')),
                ('boiler_capacity_mbh', models.FloatField(default=0, verbose_name=b'Boiler capacity (MBH)')),
                ('hours_of_operation', models.FloatField(default=8760, verbose_name=b'Yearly Hours of Operation')),
                ('separately_meter', models.IntegerField(default=0, verbose_name=b'Separately Meter', choices=[(1, b'YES'), (2, b'NO')])),
                ('make_up_water_log_separate_bill', models.IntegerField(default=0, verbose_name=b'Make Up Water Log/ Separate Bill', choices=[(1, b'YES'), (2, b'NO')])),
                ('no_of_steam_traps', models.IntegerField(default=0, verbose_name=b'Number of Steam Traps')),
                ('steam_trap_audit_performed', models.DateTimeField(default=None, verbose_name=b'Date Last Steam Trap Audit Performed')),
                ('is_the_header_insulated', models.IntegerField(default=0, verbose_name=b'Is the Header Insulated', choices=[(1, b'YES'), (2, b'NO')])),
                ('percentage_condensate_that_returns_to_boiler', models.FloatField(default=0, verbose_name=b'Percent of Condensate that returns to Boiler', choices=[(1, b'YES'), (2, b'NO')])),
                ('aerator_tank_temp', models.FloatField(default=0, verbose_name=b'Aerator Tank Temperature (small tank near boiler)')),
                ('aerator_tank_pressure', models.FloatField(default=80, verbose_name=b'Aerator Tank Pressure (small tank near boiler)')),
                ('ambient_temp', models.CharField(default=b'', max_length=128, verbose_name=b'Production Pressure, there could be multiple pressures')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='boiler_datacollection', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
