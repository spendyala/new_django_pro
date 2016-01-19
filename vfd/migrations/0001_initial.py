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
            name='LaborVFDMotor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=160, verbose_name=b'Item')),
                ('vendor', models.CharField(max_length=160, verbose_name=b'Vendor')),
                ('hourly_rate', models.FloatField(default=0, verbose_name=b'Hourly Rate')),
                ('fixed_cost', models.FloatField(default=0, verbose_name=b'Fixed Cost')),
                ('ges_cost', models.FloatField(default=0.0, verbose_name=b'GES Cost')),
                ('ges_markup', models.FloatField(default=0.0, verbose_name=b'GES Markup')),
                ('quantity', models.FloatField(default=0, verbose_name=b'Quantity')),
                ('fixed_flag', models.BooleanField(default=True, verbose_name=b'Fixed Labor Flag')),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
            ],
            options={
                'ordering': ('client_vfd',),
            },
        ),
        migrations.CreateModel(
            name='MaterialsVFDMotor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=160, verbose_name=b'Item')),
                ('supplier', models.CharField(max_length=160, verbose_name=b'Supplier')),
                ('description', models.CharField(max_length=500, verbose_name=b'Description')),
                ('ges_cost_each', models.FloatField(default=0.0, verbose_name=b'GES Cost Each')),
                ('ges_markup', models.FloatField(default=0.0, verbose_name=b'GES Markup')),
                ('quantity', models.FloatField(default=0, verbose_name=b'Quantity')),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
            ],
            options={
                'ordering': ('client_vfd',),
            },
        ),
        migrations.CreateModel(
            name='VfdMotor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vfd_name', models.CharField(max_length=256, verbose_name=b'Client VFD Name')),
                ('motor_horse_pwr', models.FloatField(default=0.0, verbose_name=b'Motor HP')),
                ('existing_motor_efficiency', models.FloatField(default=0, verbose_name=b'Existing Motor Eff. %')),
                ('proposed_vfd_efficiency', models.FloatField(default=0.0, verbose_name=b'Proposed VFD Eff. %')),
                ('motor_load', models.FloatField(default=0, verbose_name=b'Motor Load %')),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='vfd_motor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('vfd_name',),
            },
        ),
        migrations.CreateModel(
            name='VfdMotorDataPerMonth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(max_length=3, verbose_name=b'Month', choices=[(b'JAN', b'January'), (b'FEB', b'February'), (b'MAR', b'March'), (b'APR', b'April'), (b'MAY', b'May'), (b'JUN', b'June'), (b'JUL', b'July'), (b'AUG', b'August'), (b'SEP', b'September'), (b'OCT', b'October'), (b'NOV', b'November'), (b'DEC', b'December')])),
                ('hours_of_operation', models.FloatField(default=0, verbose_name=b'Hours of operation')),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('client_vfd', models.ForeignKey(to='vfd.VfdMotor')),
                ('owner', models.ForeignKey(related_name='vfd_motor_data_per_month', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('client_vfd',),
            },
        ),
        migrations.CreateModel(
            name='VfdMotorSetpointSelections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speed_percent', models.FloatField(default=0, verbose_name=b'VFD Speed %')),
                ('percent_of_time', models.FloatField(default=0, verbose_name=b'Percent Of Time (%)')),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('client_vfd', models.ForeignKey(to='vfd.VfdMotor')),
                ('owner', models.ForeignKey(related_name='vfd_motor_setpoint_selections', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('speed_percent',),
            },
        ),
        migrations.AddField(
            model_name='materialsvfdmotor',
            name='client_vfd',
            field=models.ForeignKey(to='vfd.VfdMotor'),
        ),
        migrations.AddField(
            model_name='materialsvfdmotor',
            name='owner',
            field=models.ForeignKey(related_name='materials_vfd_motor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='laborvfdmotor',
            name='client_vfd',
            field=models.ForeignKey(to='vfd.VfdMotor'),
        ),
        migrations.AddField(
            model_name='laborvfdmotor',
            name='owner',
            field=models.ForeignKey(related_name='labor_vfd_motor', to=settings.AUTH_USER_MODEL),
        ),
    ]
