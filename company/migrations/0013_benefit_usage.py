# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20161214_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefit',
            name='usage',
            field=models.IntegerField(default=0, verbose_name=b'Benefit Usage'),
            preserve_default=False,
        ),
    ]
