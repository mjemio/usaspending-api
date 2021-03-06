# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 17:56
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.management import call_command


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RefObjectClassCode',
            fields=[
                ('object_class', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('max_object_class_name', models.CharField(blank=True, max_length=60, null=True)),
                ('direct_or_reimbursable', models.CharField(blank=True, max_length=25, null=True)),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
                ('valid_begin_date', models.DateTimeField(blank=True, null=True)),
                ('valid_end_date', models.DateTimeField(blank=True, null=True)),
                ('valid_code_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('create_user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('update_user_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ref_object_class_code',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RefProgramActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_activity_code', models.CharField(max_length=4)),
                ('program_activity_name', models.CharField(max_length=164)),
                ('budget_year', models.CharField(blank=True, max_length=4, null=True)),
                ('valid_begin_date', models.DateTimeField(blank=True, null=True)),
                ('valid_end_date', models.DateTimeField(blank=True, null=True)),
                ('valid_code_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('create_user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('update_user_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ref_program_activity',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='refprogramactivity',
            unique_together=set([('program_activity_code', 'program_activity_name')]),
        ),
    ]
