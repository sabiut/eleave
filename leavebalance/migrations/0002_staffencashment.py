# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavebalance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='staffencashment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_Name', models.CharField(max_length=45)),
                ('Last_Name', models.CharField(max_length=45)),
                ('Payment_date', models.CharField(max_length=45)),
                ('Number_of_days_paid', models.IntegerField()),
                ('cheque_number', models.CharField(max_length=45)),
                ('Payment_amount', models.FloatField()),
            ],
        ),
    ]
