# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leavecurrentbalance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_Name', models.CharField(max_length=45)),
                ('Last_Name', models.CharField(max_length=45)),
                ('Leave_outstanding_balance', models.CharField(max_length=45)),
                ('Monthly_Leave_entitlement', models.CharField(max_length=45)),
                ('Monthly_leave_consumed', models.CharField(max_length=45)),
                ('Total_working_days', models.CharField(default=b'', max_length=45)),
                ('Year', models.CharField(max_length=45)),
                ('Month', models.CharField(max_length=45)),
                ('Leave_current_balance', models.CharField(max_length=45)),
            ],
        ),
    ]
