# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-18 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liana', '0002_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
