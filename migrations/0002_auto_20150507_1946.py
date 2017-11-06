# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLeave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_staff',
            name='dependants',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='new_staff',
            name='relationship_to_you',
            field=models.TextField(default=b''),
        ),
    ]
