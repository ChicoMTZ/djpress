# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-22 16:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0005_auto_20160820_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 22, 16, 41, 7, 226486, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
