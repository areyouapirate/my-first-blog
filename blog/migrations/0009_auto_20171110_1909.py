# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171110_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_group',
            new_name='gruppo',
        ),
    ]
