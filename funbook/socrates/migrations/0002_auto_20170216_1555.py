# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socrates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_body',
            field=models.TextField(max_length=1000),
        ),
    ]