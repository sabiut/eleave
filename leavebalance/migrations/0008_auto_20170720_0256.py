# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavebalance', '0007_auto_20170711_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='Select_File',
            field=models.FileField(upload_to=b'/var/www/projects/webapp/media'),
        ),
    ]
