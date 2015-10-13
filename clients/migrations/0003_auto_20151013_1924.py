# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20151013_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='customer_site',
        ),
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.TextField(default=b'', max_length=750, verbose_name=b'Address'),
        ),
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(default=b'', max_length=256, verbose_name=b'City'),
        ),
        migrations.AddField(
            model_name='client',
            name='electricity_rate',
            field=models.FloatField(default=0, verbose_name=b'Electric Rate (per kWh)'),
        ),
        migrations.AddField(
            model_name='client',
            name='facility_name',
            field=models.TextField(default=b'', max_length=750, verbose_name=b'Facility Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='gas_rate',
            field=models.FloatField(default=0, verbose_name=b'Gas Rate (MMBtu)'),
        ),
    ]
