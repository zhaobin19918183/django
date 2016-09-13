# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0043_auto_20160912_0910'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogEntry',
        ),
        migrations.AlterField(
            model_name='examinfo',
            name='level',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True),
        ),
    ]
