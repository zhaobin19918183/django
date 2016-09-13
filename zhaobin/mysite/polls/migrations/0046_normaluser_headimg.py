# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0045_remove_normaluser_headimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='headImg',
            field=models.FileField(default=1, upload_to=b'./upload'),
            preserve_default=False,
        ),
    ]
