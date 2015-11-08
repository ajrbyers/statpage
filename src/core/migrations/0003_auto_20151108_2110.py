# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_system_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'ordering': ['-started']},
        ),
        migrations.AlterField(
            model_name='incident',
            name='started',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
