# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20160829_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinfo',
            name='level',
            field=models.ImageField(height_field=b'20', upload_to=b'', width_field=b'20', verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6'),
        ),
    ]