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
            name='ValveInsulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('name', models.CharField(default=b'', max_length=128, verbose_name=b'Valve Insulation Name')),
                ('valve_type', models.CharField(default=b'', max_length=128, verbose_name=b'Valve Type')),
                ('quantity', models.IntegerField(default=0, verbose_name=b'Quantity')),
                ('nps_pipe_size_inches', models.FloatField(default=0.5, verbose_name=b'NPS Pipe Size (inches)', choices=[(0.5, 0.5), (0.75, 0.75), (1.0, 1.0), (1.25, 1.25), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (6.0, 6.0), (7.0, 7.0), (8.0, 8.0), (9.0, 9.0), (10.0, 10.0), (12.0, 12.0), (14.0, 14.0), (16.0, 16.0), (18.0, 18.0), (20.0, 20.0), (24.0, 24.0), (30.0, 30.0), (36.0, 36.0), (48.0, 48.0)])),
                ('working_fluid', models.CharField(default=b'Steam', max_length=128, verbose_name=b'Working Fluid', choices=[(b'Steam', b'Steam'), (b'Condensate', b'Condensate'), (b'Heating Hot Water', b'Heating Hot Water'), (b'Domestic Hot Water', b'Domestic Hot Water')])),
                ('process_temp_or_pressure', models.IntegerField(default=0, help_text=b'Noel Chambers: Select the temperature of the working fluid if the fluid a liquid. If the working fluid is steam please select the working pressure of the system.', verbose_name=b'Process Temp or Pressure')),
                ('system_efficiency', models.FloatField(default=80, verbose_name=b'System Efficiency')),
                ('ambient_temp', models.FloatField(default=70, verbose_name=b'Ambient Temp')),
                ('system_hours_per_year', models.FloatField(default=8760, verbose_name=b'System Hours / Year')),
                ('wind_speed_mph', models.FloatField(default=0, verbose_name=b'Wind Speed (MPH)')),
                ('location', models.CharField(default=b'Indoors', max_length=128, verbose_name=b'Location', choices=[(b'Indoors', b'Indoors'), (b'Outdoors', b'Outdoors')])),
                ('base_metal', models.CharField(default=b'Steel', max_length=128, verbose_name=b'Base Metal', choices=[(b'Steel', b'Steel'), (b'Copper', b'Copper'), (b'PVC', b'PVC')])),
                ('insulation', models.CharField(default=b'850', max_length=128, verbose_name=b'Insulation', choices=[(b'850', b'850F Mineral Fiber PIPE, Type I, C547-11'), (b'1200', b'1200F Mineral Fiber PIPE, Types II and III, C547-11'), (b'1000', b'1000F Mineral Fiber PIPE, Type IV, C547-11'), (b'Poly', b'Polystyrene PIPE, Type XIII, C578-11b')])),
                ('insulation_thickness', models.FloatField(default=0.5, verbose_name=b'Insulation Thickness', choices=[(0.5, 0.5), (0.75, 0.75), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5), (6, 6), (7, 7), (8, 8)])),
                ('jacket_material', models.CharField(default=b'', max_length=128, verbose_name=b'Jacket Material')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='valve_insulation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
