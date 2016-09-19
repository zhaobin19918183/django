# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=64)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.IntegerField(choices=[(0, '\u666e\u901a\u7528\u6237'), (1, '\u9ad8\u7ea7\u7528\u6237')])),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('user_info', models.OneToOneField(to='appTest.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='usergroup',
            name='user_info',
            field=models.ManyToManyField(to='appTest.UserInfo'),
        ),
        migrations.AddField(
            model_name='host',
            name='user_group',
            field=models.ForeignKey(to='appTest.UserGroup'),
        ),
    ]
