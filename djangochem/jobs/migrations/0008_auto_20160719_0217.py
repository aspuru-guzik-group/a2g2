# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 02:17
from __future__ import unicode_literals
import uuid

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20160719_0217'),
    ]

    operations = [
        migrations.AlterField(model_name='job',
                              name='uuid',
                              field=models.UUIDField(default=uuid.uuid4, unique=True),
                              )

    ]
