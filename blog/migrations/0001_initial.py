# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('dob_child', models.DateField(null=True, blank=True)),
                ('bio_child', models.TextField()),
                ('first_choice', models.CharField(max_length=200)),
                ('second_choice', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('typ', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('heat', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
                ('cost', models.CharField(max_length=200)),
                ('last_group', models.CharField(max_length=200)),
                ('contacts', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gruppo', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('approval', models.TextField()),
                ('img', models.ImageField(upload_to='post_img/', null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('gruppo', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('registration_date', models.DateTimeField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
