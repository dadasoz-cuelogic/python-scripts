# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import rango.models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20150520_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0, validators=[rango.models.validate_positive]),
            preserve_default=True,
        ),
    ]
