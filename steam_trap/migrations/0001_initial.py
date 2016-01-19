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
            name='SteamTrap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('steam_trap_number', models.CharField(default=b'', max_length=127, verbose_name=b'Failed Trap #')),
                ('hours_of_operation', models.IntegerField(default=8760, verbose_name=b'Hours of Operation')),
                ('boiler_efficiency', models.FloatField(default=80.0, verbose_name=b'Boiler Efficiency %')),
                ('location_description', models.CharField(default=b'', max_length=255, verbose_name=b'Location/Description')),
                ('pressure_in_psig', models.FloatField(default=100, verbose_name=b'Pressure (psig)')),
                ('trap_pipe_size', models.FloatField(default=0.5, verbose_name=b'Trap Pipe Size (inch)')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='steam_trap', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('steam_trap_number',),
            },
        ),
    ]
