# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-27 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0008_auto_20160826_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='Texto',
            field=models.TextField(),
        ),
    ]
