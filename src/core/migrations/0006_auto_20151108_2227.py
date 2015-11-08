# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151108_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='confirmation_code',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
