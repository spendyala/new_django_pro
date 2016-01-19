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
            name='StackedEconomizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('boiler_stacked_economizer', models.CharField(default=b'', max_length=128, verbose_name=b'Stacked Economizer')),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('hours_of_operations', models.FloatField(default=8760, verbose_name=b'Hours of Operation')),
                ('boiler_size_hp', models.FloatField(default=1000, verbose_name=b'Boiler Size (HP)')),
                ('initial_stack_gas_temp_f', models.FloatField(default=500, verbose_name=b'Initial Stack Gas Temp (F)')),
                ('average_fire_rate', models.FloatField(default=0, verbose_name=b'Average Fire Rate')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='stacked_economizer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('boiler_stacked_economizer',),
            },
        ),
    ]
