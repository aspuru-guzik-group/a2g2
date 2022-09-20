# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 17:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pgmols', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calc',
            name='props',
            field=django.contrib.postgres.fields.jsonb.JSONField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='mol',
            name='createtime',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='mol',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='mol',
            name='inchikey',
            field=models.CharField(db_index=True, max_length=27, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='mol',
            unique_together=set([('group', 'inchikey')]),
        ),
        migrations.AlterIndexTogether(
            name='mol',
            index_together=set([('group', 'inchikey')]),
        ),
    ]
