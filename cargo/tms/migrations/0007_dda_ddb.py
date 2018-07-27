# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-18 19:46
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0006_auto_20180718_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dda',
            fields=[
                ('ddacod', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ddacod')),
                ('ddanom', models.CharField(blank=True, db_index=True, max_length=80, verbose_name='ddanom')),
                ('ddadir', models.CharField(blank=True, max_length=80, verbose_name='ddadir')),
                ('ddapcp', models.CharField(blank=True, max_length=20, verbose_name='ddapcp')),
                ('ddapob', models.CharField(blank=True, max_length=80, verbose_name='ddapob')),
                ('ddapol', django.contrib.gis.db.models.fields.PolygonField(geography=True, srid=4326, verbose_name='ddapol')),
                ('ddatlf', models.CharField(blank=True, max_length=20, verbose_name='ddatlf')),
                ('ddafax', models.CharField(blank=True, max_length=20, verbose_name='ddafax')),
                ('ddaeml', models.EmailField(blank=True, max_length=254, verbose_name='ddaeml')),
                ('ddaestcod', models.ForeignKey(db_column='ddaestcod', null=True, on_delete=django.db.models.deletion.PROTECT, to='tms.Est')),
                ('ddapaicod', models.ForeignKey(db_column='ddapaicod', on_delete=django.db.models.deletion.PROTECT, to='tms.Pai')),
                ('ddatzncod', models.ForeignKey(db_column='pobtzncod', on_delete=django.db.models.deletion.PROTECT, to='tms.Tzn')),
            ],
        ),
        migrations.CreateModel(
            name='Ddb',
            fields=[
                ('ddbcod', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ddbcod')),
                ('ddbextcod', models.CharField(max_length=20, verbose_name='ddbextcod')),
                ('ddbclicod', models.ForeignKey(db_column='ddbclicod', on_delete=django.db.models.deletion.PROTECT, to='tms.Cli')),
                ('ddbddacod', models.ForeignKey(db_column='ddbddacod', on_delete=django.db.models.deletion.PROTECT, to='tms.Dda')),
            ],
        ),
    ]