# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0013_fiction_translation'),
    ]

    operations = [
        migrations.AddField(
            model_name='bibliography',
            name='tokenized',
            field=models.CharField(choices=[('no', 'Թոքենիզացված չէ'), ('yes', 'Թոքենիզացված է'), ('validated', 'Թոքենիզացված է, ստուգված է')], default='no', max_length=20),
        ),
    ]
