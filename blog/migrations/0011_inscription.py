# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_post_gruppo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fn_parent', models.CharField(max_length=200)),
                ('sn_parent', models.CharField(max_length=200)),
                ('fn_child', models.CharField(max_length=200)),
                ('sn_child', models.CharField(max_length=200)),
                ('dob_child', models.DateField(blank=True, null=True)),
                ('bio_child', models.TextField()),
                ('first_choice', models.CharField(max_length=200)),
                ('second_choice', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
