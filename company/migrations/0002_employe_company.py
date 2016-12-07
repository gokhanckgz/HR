# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name=b'Company ID'),
            preserve_default=False,
        ),
    ]