# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavebalance', '0006_auto_20170711_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfile',
            old_name='Select_file',
            new_name='Select_File',
        ),
    ]
