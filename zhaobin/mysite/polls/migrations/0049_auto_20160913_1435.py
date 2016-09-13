# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0048_auto_20160913_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinfo',
            name='name',
            field=models.CharField(unique=True, max_length=10, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d'),
        ),
    ]
