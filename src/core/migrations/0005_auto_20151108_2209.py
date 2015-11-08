# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='confirmation_code',
            field=models.CharField(default='dfsdfffdsf', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
