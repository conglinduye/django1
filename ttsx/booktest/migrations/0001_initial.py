# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('userver', models.CharField(default='', max_length=20)),
                ('uphon', models.CharField(default='', max_length=11)),
                ('uaddress', models.CharField(default='', max_length=40)),
                ('upcode', models.CharField(default='', max_length=10)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
