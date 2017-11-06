# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eLeave', '0002_auto_20150507_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='qualification_num1',
            field=models.CharField(max_length=45, choices=[(b'PHD Degree', b'PHD Degree'), (b'Masters Degree', b'Masters Degree'), (b'Bachelor Degree', b'Bachelor Degree'), (b'Diploma', b'Diploma'), (b'Certificate', b'Certificate'), (b'Postgraduate Diploma', b'Postgraduate Diploma')]),
        ),
        migrations.AlterField(
            model_name='training',
            name='qualification_num2',
            field=models.CharField(max_length=45, choices=[(b'PHD Degree', b'PHD Degree'), (b'Master Degree', b'Master Degree'), (b'Bachelor Degree', b'Bachelor Degree'), (b'Diploma', b'Diploma '), (b'Certificate', b'Certificate'), (b'Postgraduate Diploma', b'Postgraduate Diploma')]),
        ),
        migrations.AlterField(
            model_name='training',
            name='qualification_num3',
            field=models.CharField(max_length=45, choices=[(b'PHD Degree', b'PHD Degree'), (b'Master Degree', b'Master Degree'), (b'Bachelor Degree', b'Bachelor Degree'), (b'Diploma Degree', b'Diploma Degree'), (b'Certificate Degree', b'Certificate Degree'), (b'Postgraduate Diploma', b'Postgraduate Diploma')]),
        ),
    ]
