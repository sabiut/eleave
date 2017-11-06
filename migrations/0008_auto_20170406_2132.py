# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLeave', '0007_auto_20150618_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_staff',
            name='department',
            field=models.CharField(default=b'', max_length=45, choices=[(b'GOV', b'GOV'), (b'ACSD', b'ACSD'), (b'CSD', b'CSD'), (b'FISD', b'FISD'), (b'RSD', b'RSD'), (b'FMKD', b'FMKD')]),
        ),
        migrations.AlterField(
            model_name='newleave',
            name='department',
            field=models.CharField(max_length=45, choices=[(b'GOV', b'GOV'), (b'ACSD', b'ACSD'), (b'CSD', b'CSD'), (b'FISD', b'FISD'), (b'RHD', b'RHD'), (b'FMKD', b'FMKD')]),
        ),
        migrations.AlterField(
            model_name='newleave',
            name='leave_type',
            field=models.CharField(max_length=45, choices=[(b'Annual', b'Annual')]),
        ),
    ]
