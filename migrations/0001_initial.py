# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='employment_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution_num1', models.CharField(max_length=45)),
                ('institution_num2', models.CharField(max_length=45)),
                ('institution_num3', models.CharField(max_length=45)),
                ('position_num1', models.CharField(max_length=45)),
                ('position_num2', models.CharField(max_length=45)),
                ('position_num3', models.CharField(max_length=45)),
                ('start_Date_num1', models.DateField()),
                ('start_Date_num2', models.DateField()),
                ('start_Date_num3', models.DateField()),
                ('end_Date_num1', models.DateField()),
                ('end_Date_num2', models.DateField()),
                ('end_Date_num3', models.DateField()),
                ('responsibilities_num1', models.CharField(max_length=45)),
                ('responsibilities_num2', models.CharField(max_length=45)),
                ('responsibilities_num3', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='new_staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('gender', models.CharField(default=b'', max_length=45, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('date_of_birth', models.DateField(null=True)),
                ('marital_status', models.CharField(default=b'', max_length=45, choices=[(b'Married', b'Married'), (b'Single', b'Single')])),
                ('nationality', models.CharField(default=b'', max_length=45)),
                ('home_island', models.CharField(default=b'', max_length=45, choices=[(b'Banks', b'Banks'), (b'Santo', b'Santo'), (b'Ambae', b'Ambae'), (b'Pentecost', b'Pentecost'), (b'Maewo', b'Maewo'), (b'Malekula', b'Malekula'), (b'Ambrym', b'Ambrym'), (b'Paama', b'Paama'), (b'Epi', b'Epi'), (b'Tongoa', b'Tongoa'), (b'Tongariki', b'Tongariki'), (b'Makira', b'Makira'), (b'Emae', b'Emae'), (b'Mataso', b'Mataso'), (b'Efate', b'Efate'), (b'Erromango', b'Erromango'), (b'Tanna', b'Tanna'), (b'Futuna', b'Futuna'), (b'Aniwa', b'Aniwa')])),
                ('dependants', models.CharField(default=b'', max_length=45)),
                ('relationship_to_you', models.CharField(default=b'', max_length=45, choices=[(b'Brother', b'Brother'), (b'Sister', b'Sister'), (b'Mother', b'Mother'), (b'Father', b'Father'), (b'Ant', b'Ant'), (b'Uncle', b'Uncle'), (b'Son', b'Son'), (b'Daughter', b'Daughter'), (b'nephew', b'nephew')])),
                ('postal_Address', models.TextField(default=b'')),
                ('employee_Date', models.DateField()),
                ('position', models.CharField(max_length=45)),
                ('department', models.CharField(default=b'', max_length=45, choices=[(b'GOV', b'GOV'), (b'ACSD', b'ACSD'), (b'CSD', b'CSD'), (b'FISD', b'FISD'), (b'RSHD', b'RSHD'), (b'FMKD', b'FMKD')])),
                ('vnpf_no', models.CharField(max_length=45)),
                ('bank_name', models.CharField(default=b'', max_length=45)),
                ('account_number', models.IntegerField()),
                ('username', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='newleave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('department', models.CharField(max_length=45, choices=[(b'GOV', b'GOV'), (b'ACSD', b'ACSD'), (b'CSD', b'CSD'), (b'FISD', b'FISD'), (b'RSHD', b'RSHD'), (b'FMKD', b'FMKD')])),
                ('position', models.CharField(max_length=45)),
                ('leave_type', models.CharField(max_length=45, choices=[(b'Annual', b'Annual'), (b'Casual', b'Casual'), (b'Sick', b'Sick'), (b'Maternity', b'Maternity'), (b'Paternity', b'Paternity'), (b'Special', b'Special'), (b'Study', b'Study'), (b'Sabbatical', b'Sabbatical'), (b'Compassionate', b'Compassionate')])),
                ('specify_details', models.TextField(default=b'')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('total_working_days', models.IntegerField(null=True)),
                ('department_head_authorization', models.CharField(max_length=45, choices=[(b'Approved', b'Approved'), (b'Rejected', b'Rejected')])),
                ('authorized_by', models.CharField(default=b'', max_length=45)),
                ('remarks', models.TextField()),
                ('authorization_date', models.DateField(null=True)),
                ('corporate_services_authorization', models.CharField(max_length=45, choices=[(b'Approved', b'Approved'), (b'Rejected', b'Rejected')])),
                ('corporate_services_authorization_by', models.CharField(max_length=45)),
                ('corporate_servicesre_remarks', models.TextField(default=b'')),
                ('corporate_services_authoriztaion_date', models.DateField(null=True)),
                ('month', models.CharField(max_length=45, null=True, choices=[(b'January', b'January'), (b'February', b'February'), (b'March', b'March'), (b'April', b'April'), (b'May', b'May'), (b'June', b'June'), (b'July', b'July'), (b'August', b'August'), (b'September', b'September'), (b'October', b'October'), (b'November', b'November'), (b'December', b'December')])),
                ('year', models.CharField(max_length=45, null=True)),
                ('leave_entitlement', models.FloatField(null=True)),
                ('holiday', models.IntegerField(null=True)),
                ('weekend', models.IntegerField(null=True)),
                ('leave_outstanding_balance', models.FloatField(null=True)),
                ('leave_current_balance', models.FloatField(default=0)),
                ('staff', models.ForeignKey(default=1, to='eLeave.new_staff')),
                ('username', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution_num1', models.CharField(max_length=45)),
                ('institution_num2', models.CharField(max_length=45)),
                ('institution_num3', models.CharField(max_length=45)),
                ('qualification_num1', models.CharField(max_length=45, choices=[(b'PHD Degree', b'PHD Degree'), (b'Masters Degree', b'Masters Degree'), (b'Bachelor Degree', b'Bachelor Degree'), (b'Diploma', b'Diploma'), (b'Certificate', b'Certificate')])),
                ('qualification_num2', models.CharField(max_length=45, choices=[(b'PHD Degree', b'PHD Degree'), (b'Master Degree', b'Master Degree'), (b'Bachelor Degree', b'Bachelor Degree'), (b'Diploma Degree', b'Diploma Degree'), (b'Certificate', b'Certificate')])),
                ('qualification_num3', models.CharField(max_length=45, choices=[(b'PHD Degree', b'PHD Degree'), (b'Master Degree', b'Master Degree'), (b'Bachelor Degree', b'Bachelor Degree'), (b'Diploma Degree', b'Diploma Degree'), (b'Certificate Degree', b'Certificate Degree')])),
                ('highest_qualification', models.CharField(max_length=45)),
                ('year_of_completion_num1', models.CharField(max_length=45)),
                ('year_of_completion_num2', models.CharField(max_length=45)),
                ('year_of_completion_num3', models.CharField(max_length=45)),
                ('staff_name', models.ForeignKey(to='eLeave.new_staff')),
            ],
        ),
        migrations.AddField(
            model_name='employment_history',
            name='staff_name',
            field=models.ForeignKey(to='eLeave.new_staff'),
        ),
    ]
