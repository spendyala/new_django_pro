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
            name='AirLeak',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('air_leak', models.CharField(default=b'', max_length=128, verbose_name=b'Air Leak')),
                ('project_name', models.CharField(default=b'', max_length=128, verbose_name=b'Project Name')),
                ('leak_tag_number', models.CharField(default=b'', max_length=128, verbose_name=b'Leak Tag Number')),
                ('datetime_time_leak_found', models.DateField(null=True, verbose_name=b'Date Leak found', blank=True)),
                ('leak_area_description', models.CharField(default=b'', max_length=128, verbose_name=b'Leak Area Description')),
                ('leak_equipment_desc', models.CharField(default=b'', max_length=128, verbose_name=b'Leak Equipment Description')),
                ('leak_type', models.CharField(default=b'', max_length=128, verbose_name=b'Leak Type')),
                ('annual_hours_of_operation', models.FloatField(default=0, verbose_name=b'Annual Hours of Operation (Hours)')),
                ('leak_db_reading', models.IntegerField(default=10, verbose_name=b'Leak DB Reading', choices=[(10, 0.1), (20, 0.159), (30, 0.312), (40, 0.589), (50, 1.118), (60, 2.178), (70, 3.5), (80, 4.0), (90, 5.0), (100, 6.5)])),
                ('leak_reparied_flag', models.IntegerField(default=1, verbose_name=b'Leak Repaired?', choices=[(1, b'YES'), (2, b'NO')])),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='air_leak', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('air_leak',),
            },
        ),
    ]
