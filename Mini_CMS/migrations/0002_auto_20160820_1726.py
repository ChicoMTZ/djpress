# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 15:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Mini_CMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 20, 15, 26, 20, 192000, tzinfo=utc), verbose_name=b'Fecha de publicaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='pagina',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 20, 15, 26, 20, 192000, tzinfo=utc), verbose_name=b'Fecha de publicaci\xc3\xb3n'),
        ),
    ]