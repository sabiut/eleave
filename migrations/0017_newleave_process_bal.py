# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLeave', '0016_auto_20170914_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='newleave',
            name='process_bal',
            field=models.CharField(default=b'', max_length=45, choices=[(b'Processed', b'Processed'), (b'Revise', b'Revise')]),
        ),
    ]
