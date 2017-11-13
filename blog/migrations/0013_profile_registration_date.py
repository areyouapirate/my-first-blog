# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20171113_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='registration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
