# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20150519_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
