# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-26 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0007_auto_20160826_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='Correo',
            field=models.EmailField(max_length=254),
        ),
    ]
