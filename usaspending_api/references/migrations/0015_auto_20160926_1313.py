# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0014_auto_20160923_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalentity',
            name='division_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='division_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
