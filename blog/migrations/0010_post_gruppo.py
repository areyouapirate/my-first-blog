# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171110_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gruppo',
            field=models.CharField(default='no group', max_length=200),
            preserve_default=False,
        ),
    ]
