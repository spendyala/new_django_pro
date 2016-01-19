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
            name='SteamLeak',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('steam_leak_number', models.CharField(default=b'', max_length=127, verbose_name=b'Leak #')),
                ('location_description', models.CharField(default=b'', max_length=255, verbose_name=b'Location/Description')),
                ('pressure_in_psig', models.FloatField(default=100, verbose_name=b'Pressure (psig)')),
                ('size_leak_in_inch', models.FloatField(default=0.125, verbose_name=b'Size Leak (inch)')),
                ('hours_of_operation', models.IntegerField(default=8760, verbose_name=b'Hours of Operation')),
                ('boiler_efficiency', models.FloatField(default=80.0, verbose_name=b'Boiler Efficiency %')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='steam_leaks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('steam_leak_number',),
            },
        ),
    ]
