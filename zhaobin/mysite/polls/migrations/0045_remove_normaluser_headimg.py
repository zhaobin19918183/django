# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0044_auto_20160912_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normaluser',
            name='headImg',
        ),
    ]
