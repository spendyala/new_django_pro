# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('air_compressors', '0002_auto_20151008_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircompressor',
            name='vfd_90_t_fitting',
            field=models.IntegerField(default=1, verbose_name=b'90Degree T-fitting', choices=[(1, b'YES'), (2, b'NO')]),
        ),
        migrations.AlterField(
            model_name='aircompressor',
            name='vfd_speed_control',
            field=models.IntegerField(default=1, verbose_name=b'VFD Speed Control', choices=[(1, b'YES'), (2, b'NO')]),
        ),
    ]
