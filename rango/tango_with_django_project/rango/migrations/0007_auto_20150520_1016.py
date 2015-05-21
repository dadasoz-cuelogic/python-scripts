# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20150515_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
