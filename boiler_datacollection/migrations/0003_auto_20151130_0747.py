# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boiler_datacollection', '0002_auto_20151130_0610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boilerdatacollection',
            old_name='ambient_temp',
            new_name='production_pressure',
        ),
    ]
