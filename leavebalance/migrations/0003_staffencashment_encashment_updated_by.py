# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavebalance', '0002_staffencashment'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffencashment',
            name='encashment_updated_by',
            field=models.CharField(default=b'', max_length=45, choices=[(b'Kensen', b'Kensen'), (b'Kenny', b'Kenny'), (b'Julia', b'Julia')]),
        ),
    ]
