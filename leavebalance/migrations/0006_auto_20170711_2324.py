# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavebalance', '0005_uploadfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfile',
            old_name='docfile',
            new_name='Select_file',
        ),
    ]
