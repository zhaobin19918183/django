# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_blogspost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogspost',
            options={'ordering': ('-timestamp',)},
        ),
    ]
