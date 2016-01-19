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
            name='PremiumEfficiency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'Registered Date')),
                ('motor_name', models.CharField(max_length=160, verbose_name=b'Motor Name')),
                ('annual_operating_hours', models.FloatField(default=0, verbose_name=b'Annual Operating Hours')),
                ('motor_nameplate_hp', models.FloatField(default=0, verbose_name=b'Motor Nameplate Hp')),
                ('existing_full_load_eff', models.FloatField(default=0, verbose_name=b'Existing Full Load Efficiency')),
                ('existing_three_fourth_load_eff', models.FloatField(default=0, verbose_name=b'Existing 3/4 Load Efficiency')),
                ('existing_half_load_eff', models.FloatField(default=0, verbose_name=b'Existing 1/2 Load Efficiency')),
                ('existing_motor_purchase_price', models.FloatField(default=0, verbose_name=b'Existing Motor Purchase Price')),
                ('proposed_full_load_eff', models.FloatField(default=0, verbose_name=b'Proposed Full Load Efficiency')),
                ('proposed_three_fourth_load_eff', models.FloatField(default=0, verbose_name=b'Proposed 3/4 Load Efficiency')),
                ('proposed_half_load_eff', models.FloatField(default=0, verbose_name=b'Proposed 1/2 Load Efficiency')),
                ('proposed_motor_purchase_price', models.FloatField(default=0, verbose_name=b'Proposed Motor Purchase Price')),
                ('motor_nameplate_rpm', models.FloatField(default=0, verbose_name=b'Motor Nameplate RPMs')),
                ('client', models.ForeignKey(to='clients.Client')),
                ('owner', models.ForeignKey(related_name='premium_efficiency', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('motor_name',),
            },
        ),
    ]
