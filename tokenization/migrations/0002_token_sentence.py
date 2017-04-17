# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tokenization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='sentence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tokenization.Sentence'),
            preserve_default=False,
        ),
    ]