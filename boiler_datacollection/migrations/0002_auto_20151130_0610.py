# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boiler_datacollection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boilerdatacollection',
            name='aerator_tank_pressure',
            field=models.FloatField(default=80, help_text=b'small tank near boiler', verbose_name=b'Aerator Tank Pressure'),
        ),
        migrations.AlterField(
            model_name='boilerdatacollection',
            name='aerator_tank_temp',
            field=models.FloatField(default=0, help_text=b'small tank near boiler', verbose_name=b'Aerator Tank Temperature'),
        ),
        migrations.AlterField(
            model_name='boilerdatacollection',
            name='ambient_temp',
            field=models.CharField(default=b'', help_text=b'There could be multiple pressures', max_length=128, verbose_name=b'Production Pressure'),
        ),
        migrations.AlterField(
            model_name='boilerdatacollection',
            name='percentage_condensate_that_returns_to_boiler',
            field=models.FloatField(default=0, verbose_name=b'Percent of Condensate that returns to Boiler'),
        ),
        migrations.AlterField(
            model_name='boilerdatacollection',
            name='steam_trap_audit_performed',
            field=models.DateField(null=True, verbose_name=b'Date Last Steam Trap Audit Performed', blank=True),
        ),
    ]
