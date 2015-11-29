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
            name='BoilerStackedEconomizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('name', models.CharField(default=b'', max_length=128, verbose_name=b'Boiler Stacked Economizer Name')),
                ('boiler_size_hr', models.FloatField(default=0, verbose_name=b'Boiler Size (HP)')),
                ('initial_stack_gas_temp_f', models.FloatField(default=0, verbose_name=b'Initial Stack Gas Temp (F)')),
                ('avg_fire_rate', models.FloatField(default=0, verbose_name=b'Average Fire Rate')),
                ('hours_of_operation', models.FloatField(default=0, verbose_name=b'Hours of Operation')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='boiler_stacked_economizer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
