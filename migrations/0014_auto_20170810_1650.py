# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLeave', '0013_auto_20170810_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newleave',
            name='corporate_services_authoriztaion_date',
            field=models.DateField(default=b'2017-08-01', null=True),
        ),
    ]
