# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavebalance', '0004_leavecurrentbalance_leave_encashment'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('docfile', models.FileField(upload_to=b'home/sabiut/Documents')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
