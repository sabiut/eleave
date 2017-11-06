# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLeave', '0015_auto_20170810_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newleave',
            old_name='corporate_services_authorization_by',
            new_name='Authorization_by',
        ),
        migrations.RenameField(
            model_name='newleave',
            old_name='corporate_services_authoriztaion_date',
            new_name='Authoriztaion_date',
        ),
        migrations.RenameField(
            model_name='newleave',
            old_name='corporate_services_authorization',
            new_name='Director_authorization',
        ),
        migrations.RenameField(
            model_name='newleave',
            old_name='corporate_servicesre_remarks',
            new_name='Director_remarks',
        ),
    ]
