# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-17 19:05
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0002_auto_20180717_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pob',
            fields=[
                ('pobcod', models.BigIntegerField(default=0, primary_key=True, serialize=False, verbose_name='pobcod')),
                ('pobnom', models.CharField(max_length=80, verbose_name='pobnom')),
                ('pobloc', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326, verbose_name='pobloc')),
                ('pobestcod', models.ForeignKey(db_column='pobestcod', null=True, on_delete=django.db.models.deletion.PROTECT, to='tms.Est')),
                ('pobpaicod', models.ForeignKey(db_column='pobpaicod', on_delete=django.db.models.deletion.PROTECT, to='tms.Pai')),
                ('pobtzncod', models.ForeignKey(db_column='pobtzncod', on_delete=django.db.models.deletion.PROTECT, to='tms.Tzn')),
            ],
        ),
    ]
