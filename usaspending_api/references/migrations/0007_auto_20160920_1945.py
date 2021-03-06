# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0006_auto_20160920_1744'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='subtieragency',
            table='references_subtier_agency',
        ),
        migrations.RenameField(
            model_name='subtieragency',
            old_name='agency_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='subtieragency',
            name='agency_code',
        ),
        migrations.RemoveField(
            model_name='subtieragency',
            name='department',
        ),
        migrations.RemoveField(
            model_name='subtieragency',
            name='id',
        ),
        migrations.AddField(
            model_name='subtieragency',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtier_agencies', to='references.Agency'),
        ),
        migrations.AddField(
            model_name='subtieragency',
            name='code',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),

    ]
