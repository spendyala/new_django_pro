# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vfdmotorsetpointselections',
            options={'ordering': ('speed_percent',)},
        ),
        migrations.RemoveField(
            model_name='vfdmotorsetpointselections',
            name='select_point',
        ),
        migrations.AlterField(
            model_name='vfdmotor',
            name='motor_load',
            field=models.FloatField(default=0, verbose_name=b'Motor Load %'),
        ),
    ]
