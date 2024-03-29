# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 17:44
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgmols', '0004_auto_20160412_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calc',
            name='props',
            field=django.contrib.postgres.fields.jsonb.JSONField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='mol',
            name='details',
            field=django.contrib.postgres.fields.jsonb.JSONField(db_index=True, null=True),
        ),
        migrations.AlterIndexTogether(
            name='mol',
            index_together=set([('group', 'inchikey')]),
        ),
    ]
