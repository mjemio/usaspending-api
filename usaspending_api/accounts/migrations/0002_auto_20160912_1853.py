# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasuryappropriationaccount',
            name='treasury_account_identifier',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
