# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 17:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171108_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservacion',
            name='tiempo',
        ),
    ]
