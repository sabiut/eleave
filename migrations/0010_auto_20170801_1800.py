# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLeave', '0009_auto_20170711_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newleave',
            name='total_working_days',
            field=models.FloatField(null=True),
        ),
    ]
