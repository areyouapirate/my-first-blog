# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171121_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='capacity',
            field=models.IntegerField(),
        ),
    ]