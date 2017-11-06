# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavebalance', '0003_staffencashment_encashment_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavecurrentbalance',
            name='leave_encashment',
            field=models.CharField(default=b'', max_length=45),
        ),
    ]
