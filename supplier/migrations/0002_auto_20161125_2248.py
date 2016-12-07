# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='image',
            field=models.ImageField(null=b'True', upload_to=b'img', verbose_name=b'Image'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_image',
            field=models.ImageField(upload_to=b'img', verbose_name=b'Service Photo'),
        ),
    ]