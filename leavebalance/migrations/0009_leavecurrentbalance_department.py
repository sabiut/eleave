# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavebalance', '0008_auto_20170720_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavecurrentbalance',
            name='department',
            field=models.CharField(default=b'', max_length=45),
        ),
    ]
