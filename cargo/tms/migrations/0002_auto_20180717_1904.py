# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-17 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pob',
            name='pobestcod',
        ),
        migrations.RemoveField(
            model_name='pob',
            name='pobpaicod',
        ),
        migrations.RemoveField(
            model_name='pob',
            name='pobtzncod',
        ),
        migrations.DeleteModel(
            name='Pob',
        ),
    ]
