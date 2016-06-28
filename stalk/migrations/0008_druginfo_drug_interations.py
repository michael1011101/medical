# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stalk', '0007_auto_20160623_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='druginfo',
            name='drug_interations',
            field=models.TextField(null=True),
        ),
    ]
