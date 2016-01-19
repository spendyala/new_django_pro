# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BoilerBlowdown',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('boiler_blowdown_name', models.CharField(default=b'Boiler_', max_length=128, verbose_name=b'Boiler Blowdown Reduction and Recovery')),
                ('makeup_water_temperature', models.FloatField(default=0, verbose_name=b'Makeup Water Temperature')),
                ('existing_blowdown_frequency_per_day', models.FloatField(default=0, verbose_name=b'Existing Blowdown Frequency (Per Day)')),
                ('existing_blowdown_rate_gpm', models.FloatField(default=0, verbose_name=b'Existing Blowdown Rate (GPM)')),
                ('existing_blowdown_duration_mins', models.FloatField(default=0, verbose_name=b'Existing Blowdown Duration (minutes)')),
                ('existing_days_of_operation', models.FloatField(default=0, verbose_name=b'Existing Days of Operation')),
                ('existing_discharge_temp_in_f', models.FloatField(default=0, verbose_name=b'Existing Discharge Temp (F)')),
                ('proposed_blowdown_frequency_per_day', models.FloatField(default=0, verbose_name=b'Proposed Blowdown Frequency (Per Day)')),
                ('proposed_blowdown_rate_gpm', models.FloatField(default=0, verbose_name=b'Proposed Blowdown Rate (GPM)')),
                ('proposed_blowdown_duration_mins', models.FloatField(default=0, verbose_name=b'Proposed Blowdown Duration (minutes)')),
                ('proposed_days_of_operation', models.FloatField(default=0, verbose_name=b'Proposed Days of Operation')),
                ('proposed_discharge_temp_in_f', models.FloatField(default=0, verbose_name=b'Proposed Discharge Temp (F)')),
                ('existing_heat_recovery_efficiency_perc', models.FloatField(default=0, verbose_name=b'Existing Heat Recovery Efficiency')),
                ('proposed_heat_recovery_efficiency_perc', models.FloatField(default=0, verbose_name=b'Proposed Heat Recovery Efficiency')),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='boiler_blowdown', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('boiler_blowdown_name',),
            },
        ),
    ]
