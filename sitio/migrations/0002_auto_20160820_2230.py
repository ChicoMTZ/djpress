# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 20:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='urls',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 20, 20, 30, 57, 975000, tzinfo=utc), verbose_name=b'Fecha de publicaci\xc3\xb3n'),
        ),
    ]
