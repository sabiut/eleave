# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLeave', '0004_auto_20150510_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment_history',
            name='end_Date_num1',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='employment_history',
            name='end_Date_num2',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='employment_history',
            name='end_Date_num3',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='employment_history',
            name='start_Date_num2',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='employment_history',
            name='start_Date_num3',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='new_staff',
            name='marital_status',
            field=models.CharField(default=b'', max_length=45, choices=[(b'Married', b'Married'), (b'Single', b'Single'), (b'De Facto', b'De Facto')]),
        ),
        migrations.AlterField(
            model_name='training',
            name='qualification_num1',
            field=models.CharField(max_length=45, choices=[(b'PHD Degree', b'PHD Degree'), (b'Masters Degree', b'Masters Degree'), (b'Bachelor Degree', b'Bachelor Degree'), (b'Diploma', b'Diploma'), (b'Certificate', b'Certificate'), (b'Postgraduate Diploma', b'Postgraduate Diploma'), (b'none', b'none')]),
        ),
        migrations.AlterField(
            model_name='training',
            name='qualification_num2',
            field=models.CharField(max_length=45, choices=[(b'PHD Degree', b'PHD Degree'), (b'Master Degree', b'Master Degree'), (b'Bachelor Degree', b'Bachelor Degree'), (b'Diploma', b'Diploma '), (b'Certificate', b'Certificate'), (b'Postgraduate Diploma', b'Postgraduate Diploma'), (b'none', b'none')]),
        ),
        migrations.AlterField(
            model_name='training',
            name='qualification_num3',
            field=models.CharField(max_length=45, choices=[(b'PHD Degree', b'PHD Degree'), (b'Master Degree', b'Master Degree'), (b'Bachelor Degree', b'Bachelor Degree'), (b'Diploma', b'Diploma'), (b'Certificate', b'Certificate '), (b'Postgraduate Diploma', b'Postgraduate Diploma'), (b'none', b'none')]),
        ),
    ]
