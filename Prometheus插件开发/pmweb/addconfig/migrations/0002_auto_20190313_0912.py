# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-03-13 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addconfig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
