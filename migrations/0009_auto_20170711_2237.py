# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLeave', '0008_auto_20170406_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newleave',
            name='department',
            field=models.CharField(max_length=45, choices=[(b'GOV', b'GOV'), (b'ACSD', b'ACSD'), (b'CSD', b'CSD'), (b'FISD', b'FISD'), (b'RSD', b'RSD'), (b'FMKD', b'FMKD')]),
        ),
    ]
