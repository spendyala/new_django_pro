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
            name='AirCompressor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('air_compressor', models.CharField(default=b'', max_length=128, verbose_name=b'Air Compressor')),
                ('customer_name', models.CharField(default=b'', max_length=128, verbose_name=b'Customer Name')),
                ('customer_site', models.CharField(default=b'', max_length=128, verbose_name=b'Customer Site')),
                ('project_name', models.CharField(default=b'', max_length=128, verbose_name=b'Project Name')),
                ('compressor_name', models.CharField(default=b'', max_length=128, verbose_name=b'Compressor Name')),
                ('manufacturer', models.CharField(default=b'', max_length=128, verbose_name=b'Manufacturer')),
                ('model_info', models.CharField(default=b'', max_length=128, verbose_name=b'Model #')),
                ('serial_info', models.CharField(default=b'', max_length=128, verbose_name=b'Serial #')),
                ('compressor_type', models.CharField(default=b'REC', max_length=256, verbose_name=b'Compressor Type', choices=[(b'REC', b'Reciprocating'), (b'ROS', b'Rotary Screw'), (b'ROC', b'Rotary Centrifugal')])),
                ('vfd_speed_control', models.IntegerField(default=1, verbose_name=b'VFD Speed Control', choices=[(1, b'YES'), (2, b'NO')])),
                ('vfd_90_t_fitting', models.IntegerField(default=1, verbose_name=b'90Degree T-fitting', choices=[(1, b'YES'), (2, b'NO')])),
                ('nameplate_horsepower', models.FloatField(default=0, verbose_name=b'Nameplate Horsepower (HP)')),
                ('nameplate_max_flow', models.FloatField(default=0, verbose_name=b'Nameplate Maximum Flow (CFM)')),
                ('measured_actual_flow', models.FloatField(default=0, verbose_name=b'Measured Actual Flow (GPM)')),
                ('measured_line_pressure', models.FloatField(default=0, verbose_name=b'Measured Line Pressure (PSI)')),
                ('annual_hours_of_operation', models.FloatField(default=0, verbose_name=b'Annual Hours of Operation (Hours)')),
                ('reduce_line_pressure_to', models.FloatField(default=0, verbose_name=b'Reduced Line Pressure: To (PSI)')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='air_compressor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('compressor_name',),
            },
        ),
    ]
