# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_paper', '0008_auto_20170906_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='exampaper',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam_paper.Course'),
        ),
    ]