# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socrates', '0003_auto_20170216_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_body',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
