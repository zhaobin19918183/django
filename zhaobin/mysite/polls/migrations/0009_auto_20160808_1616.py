# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-08 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_booklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='booklist',
            name='number',
            field=models.CharField(max_length=10, verbose_name=b'\xe4\xb9\xa6\xe7\xb1\x8d\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
